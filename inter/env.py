# -*- coding:utf-8 -*-
import os
import threading
from inter.items import Table


# 存储一个session访问中所有的定义的变量
class VarEnv:
    def __init__(self):
        self._variable = dict()

    @property
    def session_id(self):
        return "%s-%s" % (os.getpid(), threading.current_thread().ident)

    def set(self, name, value):
        session_id = self.session_id
        if session_id not in self._variable:
            self._variable[session_id] = dict()
        self._variable[session_id][name] = value

    def get(self, name):
        session_id = self.session_id
        variables = self._variable.get(session_id)
        return variables and variables.get(name)


class DbEnv:
    _table_list = set()
    _table_map = dict()

    @staticmethod
    def add_table(table_name, table: Table):
        DbEnv._table_list.add(table_name)
        DbEnv._table_map[table_name] = table

    @staticmethod
    def exist_table(table_name):
        return table_name in DbEnv._table_list

    @staticmethod
    def get_table(table_name):
        return DbEnv._table_map.get(table_name)

    @staticmethod
    def remove_table(table_name):
        DbEnv._table_list.remove(table_name)
        DbEnv._table_map.pop(table_name, None)


class TableSelEnv:
    def __init__(self, parent_env=None):
        self.parent_env = parent_env
        # 包括alias和origin name
        self.tables = dict()

    def exist_table(self, table_name: str)->bool:
        if table_name in self.tables:
            return True
        if not self.parent_env:
            return False
        return table_name in self.parent_env.tables()

    def get_table(self, table_name: str):
        if table_name in self.tables:
            return self.tables.get(table_name)
        if not self.parent_env:
            return None
        return self.parent_env.tables.get(table_name)

    def set_table(self, table_name, table):
        self.tables[table_name] = table


class ColSelEnv:
    def __init__(self):
        pass







