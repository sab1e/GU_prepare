import sqlite3


class WarehouseAccounting:
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())

    def fetchall(self):
        return self.cursor.fetchall()
