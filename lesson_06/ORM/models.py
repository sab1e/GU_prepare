from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    category_name = Column(String, primary_key=True, nullable=False)
    category_description = Column(String, nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description


class Units(Base):
    __tablename__ = 'units'
    unit = Column(String, primary_key=True, nullable=False)

    def __init__(self, unit):
        self.unit = unit


class Positions(Base):
    __tablename__ = 'positions'
    position = Column(String, primary_key=True, nullable=False)

    def __init__(self, position):
        self.position = position


class Goods(Base):
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String, nullable=False)
    good_unit = Column('Units', ForeignKey('units.unit'))
    good_cat = Column('Categories', ForeignKey('categories.category_name'))

    def __init__(self, good_name, good_unit):
        self.good_name = good_name
        self.good_unit = good_unit


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String, nullable=False)
    employee_position = ('Poditions', ForeignKey('positions.position'))

    def __init__(self, employee_id, employee_fio, employee_position):
        self.employee_fio = employee_fio
        self.employee_position = employee_position


class Vendors(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String, nullable=False)
    vendor_ownerchipform = Column(String)
    vendor_address = Column(String)
    vendor_phone = Column(String)
    vendor_email = Column(String)

    def __init__(self, vendor_name, vendor_ownerchipform, vendor_address,
                 vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_ownerchipform = vendor_ownerchipform
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email
