# -*- coding:utf-8 -*-


class FuncService:
    func_map = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "%": lambda x, y: x % y,
        "in": lambda x, args: x in args,
    }

    @staticmethod
    def exec(name: str, *args, **kwargs):
        func = FuncService.func_map.get(name)
        if func is None:
            raise Exception()
        return func(*args, **kwargs)

    @staticmethod
    def register_func(name: str, func: callable):
        pass
