from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ORM.models import Base


class WarehouseAccounting:
    def __init__(self, db_path):
        engine = create_engine(db_path)
        Base.metadata.create_all(engine)
        self.__sesinon_db = sessionmaker(bind=engine)

    def get_session(self):
        return self.__sesinon_db
