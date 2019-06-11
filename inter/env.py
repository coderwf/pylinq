# -*- coding:utf-8 -*-


class DbEnv:
    pass


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







