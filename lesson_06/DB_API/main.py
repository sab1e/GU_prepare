from database import WarehouseAccounting
from query import CREATE_TABLE as queries

db_path = 'db_wharehouse.sqlite'

if __name__ == '__main__':
    with WarehouseAccounting(db_path) as db:
        for query in queries.values():
            db.execute_query(query)
