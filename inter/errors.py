# -*- coding:utf-8 -*-


class SqlError(Exception):
    def __init__(self, error_code, error_msg, *args):
        self.error_code = error_code
        self.error_msg = error_msg % args

    def __str__(self):
        return self.error_msg


class InternalError(Exception):
    def __init__(self, error_msg, *args):
        self.error_msg = error_msg % args

    def __str__(self):
        return self.error_msg


class UndefinedIdentifierError(SqlError):
    pass


class UnknownFunc(SqlError):
    pass
