from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text, Interval
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class Notebooks(Base):
    __tablename__ = "notebooks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    title = Column(String, nullable=True)
    color_hex = Column(String, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    notebook_id = Column(Integer, nullable=True)
    title = Column(String, nullable=True)
    content = Column(String, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class NoteTags(Base):
    __tablename__ = "note_tags"

    note_id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, primary_key=True)


