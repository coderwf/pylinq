# -*- coding:utf-8 -*-
from collections import namedtuple
from inter.env import TableSelEnv
from visitor.funcs import FuncService


CONST = namedtuple("const", "value verbose")

COLUMN = namedtuple("column", "table column verbose")

VARIABLE = namedtuple("variable", "name verbose")

EXPR0 = namedtuple("expr0", "func verbose")

EXPR1 = namedtuple("expr1", "func arg verbose")

EXPR2 = namedtuple("expr2", "func arg1 arg2 verbose")

EXPR3 = namedtuple("expr3", "func arg1 arg2 arg3 verbose")

EXPR = namedtuple("expr", "func args verbose")

EXPS = namedtuple("exps", "exps verbose")

VAR = namedtuple("var", "pos")

FROM_CLAUSE = namedtuple("from", "table_sources where group_by having")
LIMIT_CLAUSE = namedtuple("limit", "limit offset")
ORDER_CLAUSE = namedtuple("order", "")

SELECT_STMT = namedtuple("select", "spec elements from_clause order_clause limit_clause")


TABLE = namedtuple("table", "query name alias join_tables")

JOIN_TABLE = namedtuple("join_table", "join_type table condition")

ORDER_BY = namedtuple("order_by", "expression order")


class VarEnv:
    def __init__(self):
        self.variable = dict()

    def set(self, name, value):
        self.variable[name] = value

    def get(self, name):
        return self.variable.get(name)


class ExprCompiler:
    def __init__(self, var_env: VarEnv):
        self.varEnv = var_env
        self.colCount = 0
        self.colNameList = list()
        self.expr_map = {
            "const": self.compile_const,
            "column": self.compile_column,
            "variable": self.compile_variable,
            "expr0": self.compile_expr0,
            "expr1": self.compile_expr1,
            "expr2": self.compile_expr2,
            "expr3": self.compile_expr3,
            "expr": self.compile_expr,
            "exps": self.compile_exps,
        }

    def compile(self, expr):
        _, expr = self.compile_common(expr)
        return self.colNameList, expr

    def compile_common(self, expr):
        comp = self.expr_map.get(type(expr).__name__)
        if comp is None:
            raise Exception()
        return comp(expr)

    @staticmethod
    def compile_const(expr: CONST):
        return 0, expr

    def compile_column(self, expr: COLUMN):
        self.colNameList.append((expr.table, expr.column))
        self.colCount += 1
        return 1, VAR(self.colCount - 1)

    def compile_variable(self, expr: VARIABLE):
        value = self.varEnv.get(expr.name)
        if value is None:
            raise Exception("")
        return 0, CONST(value, expr.verbose)

    @staticmethod
    def compile_expr0(expr: EXPR0):
        return 0, CONST(FuncService.exec(expr.func), expr.verbose)

    def compile_expr1(self, expr: EXPR1):
        func = expr.func
        vn, var = self.compile_common(expr.arg)
        if vn == 0:
            return 0, FuncService.exec(func, var)
        return 1, EXPR1(func, var, expr.verbose)

    def compile_expr2(self, expr: EXPR2):
        vn1, var1 = self.compile_common(expr.arg1)
        vn2, var2 = self.compile_common(expr.arg2)
        if vn1 + vn2 == 0:
            return 0, CONST(FuncService.exec(expr.func, var1.value, var2.value), expr.verbose)
        return vn1 + vn2, EXPR2(expr.func, var1, var2, expr.verbose)

    def compile_expr3(self, expr: EXPR3):
        vn1, var1 = self.compile_common(expr.arg1)
        vn2, var2 = self.compile_common(expr.arg2)
        vn3, var3 = self.compile_common(expr.arg3)
        if vn1 + vn2 + vn3 == 0:
            return 0, CONST(FuncService.exec(expr.func, var1.value, var2.value, var3.value), expr.verbose)
        return vn1 + vn2 + vn3, EXPR3(expr.func, var1, var2, var3, expr.verbose)

    def compile_expr(self, expr: EXPR):
        var_count = 0
        args = list()
        for arg in expr.args:
            vn, var = self.compile_common(arg)
            var_count += vn
            args.append(var)
        if var_count == 0:
            return 0, CONST(FuncService.exec(expr.func, *tuple(arg.value for arg in args)), expr.verbose)
        return var_count, EXPR(expr.func, tuple(args), expr.verbose)

    def compile_exps(self, exps: EXPS):
        var_count = 0
        args = list()
        for arg in exps.exps:
            vn, var = self.compile_common(arg)
            var_count += vn
            args.append(var)
        if var_count == 0:
            return 0, CONST(tuple(arg.value for arg in args), exps.verbose)
        return var_count, EXPS(tuple(args), exps.verbose)


def visit_var(expr: VAR, values):
    return values[expr.pos]


def visit_const(expr: CONST, values):
    return expr.value


def visit_expr(expr: EXPR, *values):
    func = expr.func
    return FuncService.exec(func, *tuple(visit(arg, values) for arg in expr.args))


def visit_expr1(expr: EXPR1, *values):
    func = expr.func
    return FuncService.exec(func, visit(expr.arg, values))


def visit_expr2(expr: EXPR2, values):
    func = expr.func
    return FuncService.exec(func, visit(expr.arg1, values), visit(expr.arg2, values))


def visit_expr3(expr: EXPR3, values):
    func = expr.func
    return FuncService.exec(func, visit(expr.arg1, values), visit(expr.arg2, values), visit(expr.arg3, values))


def visit_exps(exps: EXPS, values):
    return tuple(visit(exp, values) for exp in exps.exps)


visit_map = {
    "const": visit_const,
    "var": visit_var,
    "expr": visit_expr,
    "expr1": visit_expr1,
    "expr2": visit_expr2,
    "expr3": visit_expr3,
    "exps": visit_exps
}


def visit(expr, values):
    visitor = visit_map.get(type(expr).__name__)
    try:
        res = visitor(expr, values)
    except Exception:
        raise Exception()
    return res


def visit_select_stmt(sel_stmt: SELECT_STMT, t_env: TableSelEnv):
    distinct = True if sel_stmt.spec == "distinct" else False
    elements = sel_stmt.elements
    from_clause = sel_stmt.from_clause
    limit_clause = sel_stmt.limit_clause
    order_clause = sel_stmt.order_clause


def visit_from_table(el_ts_env: TableSelEnv, table: TABLE):
    table_final_name = table.alias or table.name
    this_sel_env = TableSelEnv()
    if el_ts_env.exist_table(table_final_name):
        raise Exception("unique table name %s" % table_final_name)
    if table.query:
        table_data = visit_select_stmt(table.query, None)
    else:
        table_data = el_ts_env.get_table(table_final_name)
    this_sel_env.set_table(table_final_name, table_data)
    el_ts_env.set_table(table_final_name, table_data)
    if table.join_tables:
        pass


def visit_from_clause(from_clause: FROM_CLAUSE):
    # 先找到需要的表
    table_sources = from_clause.table_sources
    real_tables = list()
    cur_ts_env = TableSelEnv()
    for table_source in table_sources:
        pass
    # 根据where筛选出符合条件的行

    where_expr = from_clause.where

    # 根据item进行聚合
    group_by = from_clause.group_by

    # 对聚合后的数据再次进行筛选
    having_expr = from_clause.having


def visit_limit_clause():
    pass


def visit_order_clause():
    pass


def visit_clause():
    pass


if __name__ == "__main__":
    c1 = COLUMN("a", "b", "")
    c2 = COLUMN("1", "1", "")
    c = CONST(1, "")
    _, expr = ExprCompiler(VarEnv()).compile(EXPR2("in", c, EXPS((c1, c2), ""), ""))
    print(visit(expr, [1,2]))
