"""
This module was made by shout on 2025-05-03 21:31:26.603272-04:00,
using orm-maker v0.1.3,
input file: <bound method Path.absolute of PosixPath('/Users/shout/Documents/Code/Python/orm_maker/example/example.csv')>
"""

import datetime
import enum
import uuid
from typing import ClassVar, List, Optional

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BASE_VALID(enum.Enum):
    valid = "valid"
    not_valid = "not_valid"
    to_validate = "to_validate"


class TIRES_POSITION(enum.Enum):
    left_front = "left_front"
    right_front = "right_front"
    left_back = "left_back"
    right_back = "right_back"


class Base(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=lambda: uuid.uuid4())
    revby: Mapped[uuid.UUID] = mapped_column()
    revdate: Mapped[datetime.datetime] = mapped_column()
    valid: Mapped[Optional[BASE_VALID]] = mapped_column(sqlalchemy.Enum(BASE_VALID))


class CARS(Base):
    __tablename__ = "cars"
    __table_args__ = {"schema": "main"}
    made_on: Mapped[Optional[datetime.datetime]] = mapped_column()
    make: Mapped[Optional[str]] = mapped_column()
    model: Mapped[Optional[str]] = mapped_column()
    name: Mapped[str] = mapped_column()
    seats: ClassVar[Optional[List]]
    year: Mapped[Optional[int]] = mapped_column()

    def __repr__(self) -> str:
        return f"<CARS=(made_on={self.made_on}, make={self.make}, model={self.model}, year={self.year})>"

    def __eq__(self, other) -> bool:
        return type(other) is CARS and other.id == self.id


class OEM(Base):
    __tablename__ = "oem"
    __table_args__ = {"schema": "main"}
    name: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return "<OEM=()>"

    def __eq__(self, other) -> bool:
        return type(other) is OEM and other.id == self.id


class PEOPLE(Base):
    __tablename__ = "people"
    __table_args__ = {"schema": "main"}
    first: Mapped[Optional[str]] = mapped_column()

    def __repr__(self) -> str:
        return f"<PEOPLE=(first={self.first})>"

    def __eq__(self, other) -> bool:
        return type(other) is PEOPLE and other.id == self.id


class TIRES(Base):
    __tablename__ = "tires"
    __table_args__ = {"schema": "main"}
    car_id: Mapped[uuid.UUID] = mapped_column()
    made_on: Mapped[Optional[datetime.datetime]] = mapped_column()
    position: Mapped[Optional[TIRES_POSITION]] = mapped_column(sqlalchemy.Enum(TIRES_POSITION))
    rubber: Mapped[Optional[str]] = mapped_column()

    def __repr__(self) -> str:
        return f"<TIRES=(made_on={self.made_on}, position={self.position}, rubber={self.rubber})>"

    def __eq__(self, other) -> bool:
        return type(other) is TIRES and other.id == self.id


def main():
    engine = create_engine("sqlite:////Users/shout/Documents/Code/Python/orm_maker/example/example_1.sqlite", echo=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
