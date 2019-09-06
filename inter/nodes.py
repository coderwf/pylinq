# -*- coding:utf-8 -*-
import functools
from inter.env import VarEnv, DbEnv
from inter.errors import UndefinedIdentifierError
from inter.funcs import FuncService
from inter.items import Table


# join_type
class JoinType:
    inner_join = "inner_join"
    cross_join = "cross_join"
    left_join = "left_join"
    right_join = "right_join"
    straight_join = "straight_join"


# base node
class Node:

    _env = VarEnv()

    __slots__ = ["_verbose"]
    _type = "node"

    def __init__(self, verbose, *args, **kwargs):
        assert verbose
        self._verbose = verbose

    def __expr__(self):
        return self._verbose

    def __str__(self):
        return self._verbose

    @property
    def verbose(self):
        return self._verbose

    @property
    def type(self):
        return self._type


class Expr(Node):

    __slots__ = ["_verbose"]
    _type = "expr"

    def __init__(self, verbose, *args, **kwargs):
        Node.__init__(self, verbose, *args, **kwargs)

    # 将需要的变量名加到names中去,并返回table column的个数和编译后的结点
    def compile(self, *args):
        raise NotImplementedError("not implemented compile by expr")

    def _execute(self, *args):
        raise NotImplementedError("not implemented _execute by expr")

    def execute(self, *args):
        return self._execute(*args)


# const
class Const(Expr):

    __slots__ = ["_verbose", "_value"]
    _type = "const"

    def __init__(self, verbose, value):
        Expr.__init__(self, verbose)
        self._value = value

    def compile(self, *args):
        return 0, self

    def _execute(self, *args):
        return self._value


# table column
class Column(Expr):

    __slots__ = ["_verbose", "_column", "_pos"]
    _type = "column"

    def __init__(self, verbose, column):
        Expr.__init__(self, verbose)
        self._column = column
        self._pos = -1

    def compile(self, names):
        names.append(self._column)
        self._pos = len(names) - 1
        return 1, self

    def _execute(self, values):
        if isinstance(values, (list, tuple)):
            return values[self._pos]
        if isinstance(values, dict):
            value = values.get(self._column)
            if value is None:
                raise Exception("cat't get value %s" % self._column)
            return value
        raise TypeError("values must be list, tuple or dict")


# variable
class Variable(Expr):

    __slots__ = ["_var", "_verbose", "_value"]
    _type = "variable"

    def __init__(self, verbose, name):
        Expr.__init__(self, verbose)
        self._var = name
        self._value = 0

    def compile(self, *args):
        value = self._env.get(self._var)
        if value is None:
            raise UndefinedIdentifierError("undefined identifier %s", self._var)
        self._value = value
        return 0, Const(self.verbose, value)

    def _execute(self, *args):
        return self._value


class AssignExpr(Expr):
    _type = "assign"
    __slots__ = ["_verbose", "_expr", "_var_name"]

    def __init__(self, verbose, var_name, _expr: Expr):
        Expr.__init__(self, verbose)
        self._var_name = var_name
        self._expr = _expr

    def compile(self, names, group_names):
        var_count, _expr = self._expr.compile(names, group_names)
        if var_count == 0:
            return 0, Const(expr.verbose, expr.execute())
        return var_count, AssignExpr(self.verbose, self._var_name, expr)

    def _execute(self, values):
        value = self._expr.execute(values)
        self._env.set(self._var_name, value)
        return value


class Func(Expr):

    _type = "func"
    __slots__ = ["_verbose", "_func"]

    def __init__(self, verbose, func):
        Expr.__init__(self, verbose)
        self._func = func

    def execute(self, *args):
        pass

    def compile(self, *args):
        pass

    def _execute(self, *args):
        pass


# func without param
class Func0(Func):

    __slots__ = ["_verbose", "_func", "_value"]
    _type = "func0"

    def __init__(self, verbose, func):
        Expr.__init__(self, verbose)
        self._func = func
        self._value = 0

    def compile(self, *args):
        if FuncService.aggr_func(self._func):
            raise Exception("can't be aggr func")

        value = FuncService.exec(self._func)
        self._value = value
        return 0, Const(self.verbose, value)

    def _execute(self, *args):
        return self._value


class AggrFunc(Func):
    _type = "aggr_func"
    __slots__ = ("_verbose", "_func", "_expr", "_aggr_names")

    def __init__(self, verbose, func, _expr: Expr, aggr_names: set):
        Func.__init__(self, verbose, func)
        self._expr = _expr
        self._aggr_names = aggr_names

    def execute(self, values):
        expr_values = []
        value_list = tuple(values.get(name) for name in self._aggr_names)
        for args in zip(*value_list):
            new_values = dict()
            for name, value in zip(self._aggr_names, args):
                new_values[name] = value
            expr_values.append(self._expr.execute(new_values))
        return FuncService.exec(self._func, expr_values)


# func with 1 param
class Func1(Func):

    __slots__ = ["_verbose", "_func", "_expr"]
    _type = "func1"

    def __init__(self, verbose, func, _expr: Expr):
        Expr.__init__(self, verbose)
        self._func = func
        self._expr = _expr

    def compile(self, names, group_names):
        var_count, _expr = self._expr.compile(names, group_names)
        if var_count == 0:
            return 0, Const(self.verbose, FuncService.exec(self._func, expr.execute()))
        return var_count, Func1(self.verbose, self._func, expr)

    def _execute(self, values):
        arg = self._expr.execute(values)
        return FuncService.exec(self._func, arg)


# func with 2 params
class Func2(Func):

    __slots__ = ["_verbose", "_func", "_expr1", "_expr2"]
    _type = "func2"

    def __init__(self, verbose, func, expr1: Expr, expr2: Expr):
        Expr.__init__(self, verbose)
        self._func = func
        self._expr1 = expr1
        self._expr2 = expr2

    def compile(self, names):
        var_count1, expr1 = self._expr1.compile(names)
        var_count2, expr2 = self._expr2.compile(names)
        if var_count1 + var_count2 == 0:
            return 0, Const(self.verbose, FuncService.exec(self._func, expr1.execute(), expr2.execute()))
        return var_count1 + var_count2, Func2(self.verbose, self._func, expr1, expr2)

    def _execute(self, values):
        arg1 = self._expr1.execute(values)
        arg2 = self._expr2.execute(values)
        return FuncService.exec(self._func, arg1, arg2)


# func with 3 params
class Func3(Func):

    __slots__ = ["_verbose", "_func", "_expr1", "_expr2", "_expr3"]
    _type = "func3"

    def __init__(self, verbose, func, expr1: Expr, expr2: Expr, expr3: Expr):
        Expr.__init__(self, verbose)
        self._func = func
        self._expr1 = expr1
        self._expr2 = expr2
        self._expr3 = expr3

    def compile(self, names):
        var_count1, expr1 = self._expr1.compile(names)
        var_count2, expr2 = self._expr2.compile(names)
        var_count3, expr3 = self._expr3.compile(names)
        total_var_count = var_count1 + var_count2 + var_count3
        if total_var_count == 0:
            return 0, FuncService.exec(self._func, expr1.execute(), expr2.execute(), expr3.execute())
        return total_var_count, Func3(self.verbose, self._func, expr1, expr2, expr3)

    def _execute(self, values):
        arg1 = self._expr1.execute(values)
        arg2 = self._expr2.execute(values)
        arg3 = self._expr3.execute(values)
        return FuncService.exec(self._func, arg1, arg2, arg3)


# func with n params
class FuncN(Func):

    __slots__ = ["_func", "_verbose", "_exps"]
    _type = "funcN"

    def __init__(self, verbose, func, exps):
        Expr.__init__(self, verbose)
        self._func = func
        self._exps = exps

    def compile(self, names):
        total_var_count = 0
        compiled_exps = []
        for exp in self._exps:
            var_count, expr = exp.compile(names)
            total_var_count += var_count
            compiled_exps.append(expr)
        if total_var_count == 0:
            return 0, FuncService.exec(self._func, *tuple(expr.execute() for expr in compiled_exps))

        return FuncN(self.verbose, self._func, compiled_exps)

    def _execute(self, values):
        args = tuple(expr.execute(values) for expr in self._exps)
        return FuncService.exec(self._func, *args)


class Consts(Expr):

    _type = "consts"
    __slots__ = ["_verbose", "_values"]

    def __init__(self, verbose, values):
        Expr.__init__(self, verbose)
        self._values = values

    def compile(self, *args):
        return 0, self

    def _execute(self, *args):
        return self._values


# exps
class Exps(Expr):
    _type = "exps"
    __slots__ = ["_verbose", "_exps"]

    def __init__(self, verbose, exps):
        Expr.__init__(self, verbose)
        self._exps = exps

    def compile(self, names):
        compiled_exps = []
        total_var_count = 0

        for exp in self._exps:
            var_count, _expr = exp.compile(names)
            total_var_count += var_count
            compiled_exps.append(_expr)
        if total_var_count == 0:
            values = tuple(_expr.execute() for _expr in compiled_exps)
            return 0, Consts(self.verbose, values)
        return total_var_count, Exps(self.verbose, compiled_exps)

    def _execute(self, values):
        return tuple(_expr.execute(values) for _expr in self._exps)


"""
join table with condition filter
"""


# 直接笛卡尔乘积
def _cross_join(a_table: Table, b_table: Table, r_table: Table):
    a_table_rows, b_table_rows = a_table.get_rows(), b_table.get_rows()
    for a_table_row in a_table_rows:
        for b_table_row in b_table_rows:
            r_row = a_table_row.copy()
            r_row.extend(b_table_row)
            r_table.add_row_list(r_row)
    return r_table


def _cross_join_on_condition(a_table: Table, b_table: Table, r_table: Table, names, condition: Expr):
    a_table_rows, b_table_rows = a_table.get_rows(), b_table.get_rows()
    a_table_rows_map_list, b_table_rows_map_list = a_table.get_rows_map_list(names), b_table.get_rows_map_list(names)
    for a_table_row, a_table_row_map in zip(a_table_rows, a_table_rows_map_list):
        for b_table_row, b_table_row_map in zip(b_table_rows, b_table_rows_map_list):
            values = a_table_row_map.copy()
            values.update(b_table_row_map)
            if not condition.execute(values):
                continue
            new_row = a_table_row.copy()
            new_row.extend(b_table_row)
            r_table.add_row_list(new_row)
    return r_table


def _a_left_join_b_on_condition(a_table: Table, b_table: Table, r_table: Table, names, condition: Expr):
    a_table_rows, b_table_rows = a_table.get_rows(), b_table.get_rows()
    a_table_rows_map_list, b_table_rows_map_list = a_table.get_rows_map_list(names), b_table.get_rows_map_list(names)
    for a_table_row, a_table_row_map in zip(a_table_rows, a_table_rows_map_list):
        find = False
        for b_table_row, b_table_row_map in zip(b_table_rows, b_table_rows_map_list):
            values = a_table_row_map.copy()
            values.update(b_table_row_map)
            if not condition.execute(values):
                continue
            find = True
            new_row = a_table_row.copy()
            new_row.extend(b_table_row)
            r_table.add_row_list(new_row)
        if not find:
            new_row = a_table_row.copy()
            r_table.add_row_list(new_row)
    return r_table


def _a_right_join_b_on_condition(a_table: Table, b_table: Table, r_table: Table, names, condition: Expr):
    a_table_rows, b_table_rows = a_table.get_rows(), b_table.get_rows()
    a_table_rows_map_list, b_table_rows_map_list = a_table.get_rows_map_list(names), b_table.get_rows_map_list(names)
    for b_table_row, b_table_row_map in zip(b_table_rows, b_table_rows_map_list):
        find = False
        for a_table_row, a_table_row_map in zip(a_table_rows, a_table_rows_map_list):
            values = a_table_row_map.copy()
            values.update(b_table_row_map)
            if not condition.execute(values):
                continue
            new_row = a_table_row.copy()
            new_row.extend(b_table_row)
            r_table.add_row_list(new_row)
        if not find:
            new_row = b_table_row.copy()
            r_table.add_row_list(new_row, header=True)
    return r_table


def _a_left_join_b_false(a_table: Table, r_table: Table):
    a_table_rows = a_table.get_rows()
    for a_table_row in a_table_rows:
        r_table.add_row_list(a_table_row)
    return r_table


def _a_right_join_b_false(b_table: Table, r_table: Table):
    b_table_rows = b_table.get_rows()
    for b_table_row in b_table_rows:
        r_table.add_row_list(b_table_row, header=True)
    return r_table


def outer_join(a_table: Table, b_table: Table, r_table: Table, condition: Expr, join_type):
    names = []
    var_count, condition = condition.compile(names)
    if var_count > 0:
        if join_type == JoinType.left_join:
            return _a_left_join_b_on_condition(a_table, b_table, r_table, names, condition)
        return _a_right_join_b_on_condition(a_table, b_table, r_table, names, condition)

    value = condition.execute()
    # like cross join
    if value:
        return _cross_join(a_table, b_table, r_table)
    # always false
    if join_type == JoinType.left_join:
        return _a_left_join_b_false(a_table, r_table)
    return _a_right_join_b_false(b_table, r_table)


def cross_join(a_table: Table, b_table: Table, r_table: Table, condition: Expr):
    if condition is None:
        return _cross_join(a_table, b_table, r_table)
    names = []
    var_count, condition = condition.compile(names)
    if var_count > 0:
        return _cross_join_on_condition(a_table, b_table, r_table, names, condition)
    value = condition.execute()
    if value:
        return _cross_join(a_table, b_table, r_table)
    # always false
    return r_table


def join_table(a_table: Table, b_table: Table, join_type, condition: Expr = None):
    a_table_columns = a_table.full_columns()
    b_table_columns = b_table.full_columns()
    r_table_columns = a_table_columns.copy()
    r_table_columns.extend(b_table_columns)
    r_table = Table("", columns=r_table_columns)
    if join_type == JoinType.inner_join or join_type == JoinType.cross_join or join_type == JoinType.straight_join:
        return cross_join(a_table, b_table, r_table, condition)
    return outer_join(a_table, b_table, r_table, condition, join_type)


def condition_filter(a_table: Table, r_table: Table, condition: Expr):
    names = []
    var_count, new_condition = condition.compile(names)

    if var_count == 0:
        value = new_condition.execute()
        if value:
            return r_table.set_rows_list(a_table.get_rows(copy=False))
        return r_table

    a_table_rows, a_table_rows_map_list = a_table.get_rows(copy=False), a_table.get_rows_map_list(names)
    for a_table_row, a_table_row_map in zip(a_table_rows, a_table_rows_map_list):
        if new_condition.execute(a_table_row_map):
            r_table.add_row_list(a_table_row, copy=False)
    return r_table


class Clause(Node):
    def __init__(self, verbose, *args, **kwargs):
        Node.__init__(self, verbose, *args, **kwargs)

    def execute(self, *args, **kwargs):
        raise NotImplementedError("unimplemented clause execute")


class TableSources(Node):
    def __init__(self, verbose, table_sources, var_env, *args, **kwargs):
        Node.__init__(self, verbose, *args, **kwargs)
        self._var_env = var_env
        self._table_sources = table_sources

    def _execute_source(self):
        pass

    def execute(self):
        self._execute_source()


# table_source可能是一个已经存在的table也可能是一个子查询后生成的table
# 已经存在的一个table
class TableSource(Node):

    def __init__(self, verbose, *args, join_type=None, condition=None,  **kwargs):
        Node.__init__(self, verbose, *args, **kwargs)
        self._table = None
        self._join_type = join_type
        self._condition = condition

    def execute(self, table_env):
        raise NotImplementedError("unimplemented TableSource.execute")


class CommonTableSource(TableSource):
    def __init__(self, verbose, table_name, alias, join_type=None, condition=None):
        TableSource.__init__(self, verbose, join_type=join_type, condition=condition)
        self._table_name = table_name
        self._alias = alias

    def execute(self, table_env):
        pass


# 子查询以后生成的source
class QueryTableSource(TableSource):
    def __init__(self, verbose, query, alias, join_type=None, condition=None):
        TableSource.__init__(self, verbose, join_type=join_type, condition=condition)
        self._query = query
        self._alias = alias

    def execute(self, table_env):
        pass


class WhereClause(Clause):

    _type = "where_clause"
    __slots__ = ["_verbose", "_expr"]

    def __init__(self, verbose, where_expr: Expr):
        Clause.__init__(self, verbose)
        self._expr = where_expr

    def execute(self, a_table: Table):
        if self._expr is None:
            return a_table
        r_table = Table(a_table.table_name, columns=a_table.columns)
        return condition_filter(a_table, r_table, self._expr)


class HavingClause(Clause):
    _type = "having"
    __slots__ = []

    def __init__(self, verbose):
        Clause.__init__(self, verbose)

    def execute(self, *args, **kwargs):
        pass


class LimitClause(Clause):
    def __init__(self, verbose, limit, offset):
        Clause.__init__(self, verbose)
        self._limit = limit
        self._offset = offset

    def execute(self, r_table: Table):
        new_table = Table(table_name=r_table.table_name, columns=r_table.columns)
        table_rows = r_table.get_rows(self._limit, self._offset)
        for table_row in table_rows:
            new_table.add_row_list(table_row, copy=False)
        return new_table


class OrderItem(Node):
    _type = "order_item"
    __slots__ = ["_verbose", "_expr", "_asc"]

    def __init__(self, verbose, expr: Expr, asc: bool):
        Node.__init__(self, verbose)
        self._expr = expr
        self._asc = asc

    def execute(self):
        names = []
        var_count, expr_ = self._expr.compile(names)
        return var_count, names, expr_, self._asc


class OrderClause(Clause):

    _type = "order_clause"
    __slots__ = ["_verbose", "_order_items"]

    def __init__(self, verbose, order_items):
        Clause.__init__(self, verbose)
        self._order_items = order_items

    @staticmethod
    def _sort(rows_expr_res, asc_infos):

        def _compile(row1, row2):
            for left_val, right_val, asc in zip(row1[:-1], row2[:-1], asc_infos):
                if left_val == right_val:
                    continue
                if left_val < right_val:
                    return -1 if asc else 1
                return -1 if not asc else 1
            return 0

        rows_expr_res = sorted(rows_expr_res, key=functools.cmp_to_key(_compile))

        return rows_expr_res

    @staticmethod
    def _get_rows_by_order(rows_expr_res, rows):
        new_rows = []
        for row_expr_res in rows_expr_res:
            new_rows.append(rows[row_expr_res[-1]])
        return new_rows

    def _get_rows_expr_res_and_asc_info(self, a_table: Table):
        all_names = set()

        com_items = []

        for order_item in self._order_items:
            var_count, names, expr_, asc = order_item.execute()
            all_names.update(set(names))
            com_items.append((var_count, names, expr_, asc))
        all_rows_map = a_table.get_rows_map_list(all_names)
        rows_expr_res = []

        for index, row_value_map in enumerate(all_rows_map):
            row_expr_res = []
            for _, names, expr_, _ in com_items:
                row_expr_res.append(expr_.execute(row_value_map))
            row_expr_res.append(index)
            rows_expr_res.append(row_expr_res)

        asc_infos = []
        for _, _, _, asc in com_items:
            asc_infos.append(asc)

        return rows_expr_res, asc_infos

    def execute(self, a_table: Table):
        if a_table.empty():
            return a_table

        all_rows = a_table.get_rows(copy=False)

        rows_expr_res, asc_infos = self._get_rows_expr_res_and_asc_info(a_table)
        rows_expr_res = self._sort(rows_expr_res, asc_infos)
        new_rows = self._get_rows_by_order(rows_expr_res, all_rows)
        a_table.clear()
        a_table.set_rows_list(new_rows)
        return a_table


def _group_by_one_index(rows, index):
    """
    只按照某一个字段进行聚合
    :param rows:
    :param index:
    :return:
    """
    # value - pos map
    vp_map = {}
    new_grouped_res = []
    new_add_index = 0
    for row_expr_res in rows:
        value = row_expr_res[index]
        pos = vp_map.get(value)
        if pos is None:
            new_grouped_res.append([row_expr_res])
            vp_map[value] = new_add_index
            new_add_index += 1
        else:
            add_list = new_grouped_res[pos]
            add_list.append(row_expr_res)
    return new_grouped_res


def _group_grouped_rows_by_one_index(grouped_rows, index):
    """
    对已经聚合后的rows进行下一次聚合
    :param grouped_rows:
    :param index:
    :return:
    """
    new_grouped_rows = []
    for grouped_row in grouped_rows:
        new_grouped_rows.extend(_group_by_one_index(grouped_row, index))
    return new_grouped_rows


def _group_rows(rows, start, end):
    """
    按照包括start-end之间value来聚合rows,包括start和end列
    :param rows:
    :param start:
    :param end:
    :return:
    """
    grouped_rows = _group_by_one_index(rows, start)
    for index in range(start+1, end + 1):
        grouped_rows = _group_grouped_rows_by_one_index(grouped_rows, index)
    return grouped_rows


class GroupClause(OrderClause):
    _type = "group_clause"

    def __init__(self, verbose, order_items):
        OrderClause.__init__(self, verbose, order_items)

    @staticmethod
    def _get_grouped_rows_by_order(grouped_orders, rows):
        new_rows = []
        for grouped_order in grouped_orders:
            new_row = []
            for order in grouped_order:
                new_row.append(rows[order[-1]])
            new_rows.append(new_row)
        return new_rows

    def execute(self, a_table: Table):
        if a_table.empty():
            return a_table
        all_rows = a_table.get_rows(copy=False)

        rows_expr_res, asc_infos = self._get_rows_expr_res_and_asc_info(a_table)
        rows_expr_res = self._sort(rows_expr_res, asc_infos)

        grouped_orders = _group_rows(rows_expr_res, 0, len(self._order_items) - 1)

        grouped_rows = self._get_grouped_rows_by_order(grouped_orders, all_rows)

        a_table.clear()
        a_table.set_rows_list(grouped_rows)
        return a_table


class Distinct(Node):
    def __init__(self, verbose):
        Node.__init__(self, verbose)

    def execute(self, a_table: Table):
        rows = a_table.get_rows(copy=False)
        columns_len = len(a_table.columns)

        grouped_rows = _group_rows(rows, 0, columns_len - 1)
        # 选择每个组的第一条

        new_rows = []
        for rows in grouped_rows:
            new_rows.append(rows[0])

        a_table.clear()
        a_table.set_rows_list(new_rows)
        return a_table


class Element(Node):
    _type = "element"

    def __init__(self, verbose):
        Node.__init__(self, verbose)

    # 返回需要的原始column_names, 别名names
    def compile(self, table: Table):
        raise NotImplementedError("unimplemented Element.compile")

    def execute(self):
        raise NotImplementedError("unimplemented Element.execute")


class StarElement(Element):
    _type = "star element"

    def __init__(self, verbose):
        Element.__init__(self, verbose)

    def compile(self, table: Table):
        pass

    def execute(self):
        pass


class ColumnElement(Element):
    _type = "column element"

    def __init__(self, verbose):
        Element.__init__(self, verbose)

    def compile(self, table: Table):
        pass


class FuncElement(Element):
    _type = "func element"

    def __init__(self, verbose):
        Element.__init__(self, verbose)

    def compile(self, table: Table):
        pass

    def execute(self):
        pass


class Elements(Node):
    _type = "elements"

    def __init__(self, verbose):
        Node.__init__(self, verbose)

    def compile(self, table: Table):
        pass

    def execute(self, table: Table):
        pass


class AssignElement(Element):
    _type = "assign element"

    def __init__(self, verbose):
        Element.__init__(self, verbose)

    def compile(self, table: Table):
        pass

    def execute(self):
        pass


class Stmt(Node):
    def __init__(self, verbose, *args, **kwargs):
        Node.__init__(self, verbose, *args, **kwargs)

    def execute(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    class_table = Table("class", columns=["id", "class_name", "class_number", "grade"])
    student_table = Table("student", columns=["id", "name", "mentor_id", "class_id"])

    class_table.add_row_list([1, "1班", 1, 1])
    class_table.add_row_list([2, "2班", 1, 1])
    class_table.add_row_list([3, "3班", 2, 1])
    class_table.add_row_list([4, "4班", 2, 2])
    class_table.add_row_list([5, "5班", 2, 1])
    class_table.add_row_list([6, "6班", 1, 2])
    class_table.add_row_list([7, "7班", 2, 2])
    class_table.add_row_list([8, "8班", 2, 3])

    class_table.add_row_list([8, "8班", 2, 3])
    student_table.add_row_list([1, "王小明", 1, 2])
    student_table.add_row_list([2, '张大鹏', 2, 5])
    student_table.add_row_list([3, "胡志宁", 3, 3])
    student_table.add_row_list([4, "张翠山", 3, 4])
    student_table.add_row_list([5, "张江", 4, 6])
    student_table.add_row_list([6, "王大富", 6, 3])
    student_table.add_row_list([7, "冯大春", 5, 1])
    student_table.add_row_list([9, "张大长", 2, 7])

    c1 = Column("class.id", "class.id")
    c2 = Column("student.id", "student.id")
    f1 = Func2("+", "+", c1, c2)
    f2 = Func2(">", ">", f1, Const("20", 12),)

    cc = Column("class.class_number", "class.class_number")
    cc2 = Column("class.grade", "class.grade")
    expr = Func2("+", "+", cc, cc2)

    expr2 = Func2("=", "=", expr, Const("c", 5))

    o_item1 = OrderItem("order_item", cc2, True)
    o_item2 = OrderItem("order_item", cc, False)
    r = OrderClause("order", [o_item1]).execute(class_table)

    print(r)
    wc = WhereClause("wc", expr2)

    print(class_table)
    # 按照grade聚合
    # res = GroupClause("group_clause", [o_item1]).execute(class_table)
    # print(res)

    # 按照grade和class_number聚合
    print(class_table)
    print(">>", Distinct("verbose").execute(class_table))
    res = GroupClause("group_clause", [o_item1, o_item2]).execute(class_table)
    print(res)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(res)
    # 按照class_number聚合
    # print(res.get_rows_by_columns(["class.id", "class.grade"]))

    for arg in zip([1,2], [2,3], [4, 4]):
        print(arg)







