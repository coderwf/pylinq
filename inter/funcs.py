# -*- coding:utf-8 -*-
from inter.errors import UnknownFunc
from collections import namedtuple

FUNC = namedtuple("func", ("func", "aggr"))


# not aggr func
build_in_funcs = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "**": lambda x, y: x**y,
    "%": lambda x, y: x % y,
    "mod": lambda x, y: x % y,
    "mul": lambda x, y: x * y,
    "sub": lambda x, y: x - y,
    "div": lambda x, y: x / y,
    "add": lambda x, y: x + y,
    "pow": lambda x, y: x**y,
    "in": lambda x, y: x in y,
    "is": lambda x, y: x is y,
    "=": lambda x, y: x == y,
    "==": lambda x, y: x == y,
    "|": lambda x, y: x | y,
    "&": lambda x, y: x & y,
    "^": lambda x, y: x ^ y,
    "||": lambda x, y: x or y,
    "&&": lambda x, y: x and y,
    "and": lambda x, y: x and y,
    "or": lambda x, y: x or y,
    "!": lambda x: not x,
    "not": lambda x: not x,
    "~": lambda x: ~x,
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,

}


build_in_aggr_funcs = {
    "sum": lambda x: sum(x),
    "avg": lambda x: sum(x) / len(x),
    "count": lambda x: len(x),
    "max": lambda x: max(x),
    "min": lambda x: min(x),

}


def pack_funcs(funcs: dict, aggr):
    return {func_name: FUNC(func, aggr) for func_name, func in funcs.items()}


class FuncService:
    _funcs_map = dict()
    _funcs_map.update(pack_funcs(build_in_funcs, aggr=False))
    _funcs_map.update(pack_funcs(build_in_aggr_funcs, aggr=True))

    @staticmethod
    def exec(func_name, *args, **kwargs):
        func_name = func_name.lower()
        func_node = FuncService._funcs_map.get(func_name)
        if func_node is None:
            raise UnknownFunc(100, "unknown func %s", func_name)
        return func_node.func(*args, **kwargs)

    @staticmethod
    def aggr_func(func_name):
        func_name = func_name.lower()
        func_node = FuncService._funcs_map.get(func_name)
        if func_node is None:
            raise UnknownFunc(100, "unknown func %s", func_name)
        return func_node.aggr

    @staticmethod
    def register_func(func_name, func, aggr=False):
        func_name = func_name.lower()
        if func_name in FuncService._funcs_map:
            raise Exception("func %s already exists" % func_name)
        if not callable(func):
            raise Exception("func %s is not callable" % func_name)

        FuncService._funcs_map[func_name] = FUNC(func, aggr)


# decorator
def register_func(func_name, aggr=False):
    def wrap(func):
        FuncService.register_func(func_name, func, aggr)
        return func
    return wrap
