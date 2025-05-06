'''
This module was made by shout on 2025-05-06 10:03:42.995770-04:00,
using orm-maker v0.1.19,
input file: <bound method Path.absolute of PosixPath('/Users/shout/Documents/Code/Python/orm_maker/example/example.csv')>
'''


from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional, Dict, ClassVar, TypeAlias
import datetime
import enum
import sqlalchemy
import uuid


class BASE_VALID(enum.Enum):
    VALID = 0
    NOT_VALID = 1
    TO_VALIDATE = 2

class TIRES_POSITION(enum.Enum):
    LEFT_FRONT = 0
    RIGHT_FRONT = 1
    LEFT_BACK = 2
    RIGHT_BACK = 3


class Base(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=lambda: uuid.uuid4())
    revby: Mapped[uuid.UUID] = mapped_column()
    revdate: Mapped[datetime.datetime] = mapped_column()
    valid: Mapped[Optional[BASE_VALID]] = mapped_column(sqlalchemy.Enum(BASE_VALID))


class CARS(Base):

    __tablename__ = 'cars'
    __table_args__ = {'schema': 'main'}
    made_on: Mapped[Optional[datetime.datetime]] = mapped_column()
    make: Mapped[Optional[str]] = mapped_column()
    model: Mapped[Optional[str]] = mapped_column()
    name: Mapped[str] = mapped_column()
    seats: ClassVar[Optional[list]]
    year: Mapped[Optional[int]] = mapped_column()

    def __repr__(self) -> str:
        return f'<CARS=(made_on={self.made_on}, make={self.make}, model={self.model}, year={self.year})>'



class PEOPLE(Base):

    __tablename__ = 'people'
    __table_args__ = {'schema': 'main'}
    first: Mapped[Optional[str]] = mapped_column()
    relatives: ClassVar[Optional[dict]]

    def __repr__(self) -> str:
        return f'<PEOPLE=(first={self.first})>'



class TIRES(Base):

    __tablename__ = 'tires'
    __table_args__ = {'schema': 'main'}
    car_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey('main.cars.id'))
    cars = relationship('CARS' , foreign_keys=[car_id])
    made_on: Mapped[Optional[datetime.datetime]] = mapped_column()
    position: Mapped[Optional[TIRES_POSITION]] = mapped_column(sqlalchemy.Enum(TIRES_POSITION))
    rubber: Mapped[Optional[str]] = mapped_column(String, ForeignKey('main.cars.name'))
    cars = relationship('CARS' , foreign_keys=[rubber])

    def __repr__(self) -> str:
        return f'<TIRES=(made_on={self.made_on}, position={self.position}, rubber={self.rubber})>'



ORMClass: TypeAlias = (CARS
    |PEOPLE
    |TIRES)


def make_db():
    engine = create_engine('sqlite:////Users/shout/Documents/Code/Python/orm_maker/example/example.sqlite', echo=True)
    Base.metadata.create_all(engine)

def main():
    make_db()

if __name__ == '__main__':
    main()