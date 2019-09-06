# -*- coding:utf-8 -*-


class Table:
    def __init__(self, table_name, *args, columns=None, **kwargs):
        self._table_name = table_name
        columns = columns or []
        self._columns = columns
        self._rows = []
        self._columns_len = len(self._columns)

    def clear(self):
        self._rows = []

    def empty(self):
        return len(self._rows) == 0

    @property
    def table_name(self):
        return self._table_name

    @property
    def columns(self):
        return self._columns

    def add_column(self, name):
        if name in self._columns:
            raise Exception("exist column %s" % name)
        self._columns_len += 1
        self._columns.append(name)

    def exist_column(self, name):
        return name in self._columns

    def full_columns(self):
        if self._table_name == "":
            return self._columns.copy()
        return ["%s.%s" % (self._table_name, _column) for _column in self._columns]

    def _check_columns(self, b, columns):
        a_full_columns = set(self.full_columns())
        b_full_columns = set(b.full_columns())
        full_columns = a_full_columns.intersection(b_full_columns)
        for column in columns:
            if column not in full_columns:
                raise Exception("")

    def add_row_list(self, row: list, default=None, header=False, copy=True):
        if copy:
            new_row = row.copy()
        else:
            new_row = row
        default_len = self._columns_len - len(new_row)
        if default_len > 0:
            add_elements = [default for i in range(default_len)]
            if header:
                add_elements.extend(new_row)
                new_row = add_elements
            else:
                new_row.extend(add_elements)

        self._rows.append(new_row)

    def add_row_dict(self, row: dict, default=None):
        new_row = []
        for column in self._columns:
            new_row.append(row.get(column, default))
        self._rows.append(new_row)

    def get_rows_by_columns(self, need_columns, limit=None, offset=None):
        t_rows = self._rows
        if limit is not None and offset is not None:
            t_rows = t_rows[offset: offset + limit]
        indexes = []
        full_columns = self.full_columns()

        for column in need_columns:
            if column in full_columns:
                indexes.append(full_columns.index(column))

        new_rows = []
        for row in t_rows:
            new_row = []
            for index in indexes:
                new_row.append(row[index])
            new_rows.append(new_row)
        return new_rows

    def get_rows(self, limit=None, offset=None, copy=True):
        t_rows = self._rows
        if limit is not None and offset is not None:
            t_rows = t_rows[offset: offset + limit]
        if not copy:
            return t_rows

        rows = []
        for row in t_rows:
            rows.append(row.copy())
        return rows

    def get_rows_map_list(self, need_columns, limit=None, offset=None):
        t_rows = self._rows
        if limit is not None and offset is not None:
            t_rows = t_rows[offset: offset + limit]
        rows_map_list = []
        indexes = []
        full_columns = self.full_columns()

        for column in need_columns:
            if column in full_columns:
                indexes.append(full_columns.index(column))

        for row in t_rows:
            rows_map = dict()
            for index in indexes:
                rows_map[full_columns[index]] = row[index]
            rows_map_list.append(rows_map)
        return rows_map_list

    def set_rows_list(self, rows):
        self._rows = rows

    def add_rows_list(self, rows, copy=False):
        if not copy:
            self._rows.extend(rows)
            return
        for row in rows:
            self._rows.append(row.copy())

    def __str__(self):
        res = ""
        headers = str(self.full_columns()) + "\n"
        res += headers
        for row in self._rows:
            res += str(row) + "\n"
        return res

    def __expr__(self):
        return self.__str__()


if __name__ == "__main__":
    t = Table("teacher", columns=["age", "class_id", "address"])
    t.add_row_list([1, 2, "wuhan"])
    t.add_row_list([2, 3, "xian"])
    t.add_row_dict({"age": 3})
    t.add_column("gender")
    print(t.get_rows_map_list(["age", "address", "class_id"]))
    print(t.get_rows())