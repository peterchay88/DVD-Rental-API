from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class from sqlalchemy for other tables to inherit"""
    pass