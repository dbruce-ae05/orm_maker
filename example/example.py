'''
This module was made by shout on 2025-05-13 15:45:02.225808-04:00,
using orm-maker v0.1.28,
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
        return f'<CARS=(make={self.make}, model={self.model}, made_on={self.made_on}, year={self.year}, seats={self.seats}, valid={self.valid}, revby={self.revby}, revdate={self.revdate})>'

    def update_object(self, obj) -> bool:
        if not isinstance(obj, CARS):
            return False

        self.made_on = obj.made_on
        self.make = obj.make
        self.model = obj.model
        self.name = obj.name
        self.seats = obj.seats
        self.year = obj.year
        self.id = obj.id
        self.revby = obj.revby
        self.revdate = obj.revdate
        self.valid = obj.valid

        return True


class PEOPLE(Base):

    __tablename__ = 'people'
    __table_args__ = {'schema': 'main'}
    first: Mapped[Optional[str]] = mapped_column()
    relatives: ClassVar[Optional[dict]]

    def __repr__(self) -> str:
        return f'<PEOPLE=(first={self.first}, valid={self.valid}, revby={self.revby}, revdate={self.revdate})>'

    def update_object(self, obj) -> bool:
        if not isinstance(obj, PEOPLE):
            return False

        self.first = obj.first
        self.relatives = obj.relatives
        self.id = obj.id
        self.revby = obj.revby
        self.revdate = obj.revdate
        self.valid = obj.valid

        return True


class TIRES(Base):

    __tablename__ = 'tires'
    __table_args__ = {'schema': 'main'}
    car_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey('main.cars.id', name='fk_1b7905e1-ca18-49ff-aca3-ab87b7cfc86e'))
    cars = relationship('CARS' , foreign_keys=[car_id])
    made_on: Mapped[Optional[datetime.datetime]] = mapped_column()
    position: Mapped[Optional[TIRES_POSITION]] = mapped_column(sqlalchemy.Enum(TIRES_POSITION, schema='main'))
    rubber: Mapped[Optional[str]] = mapped_column(String, ForeignKey('main.cars.name', name='fk_5eb28dc8-5c35-40e3-a040-16e17d8e8df1'))
    cars = relationship('CARS' , foreign_keys=[rubber])

    def __repr__(self) -> str:
        return f'<TIRES=(rubber={self.rubber}, car_id={self.car_id}, made_on={self.made_on}, position={self.position}, valid={self.valid}, revby={self.revby}, revdate={self.revdate})>'

    def update_object(self, obj) -> bool:
        if not isinstance(obj, TIRES):
            return False

        self.car_id = obj.car_id
        self.made_on = obj.made_on
        self.position = obj.position
        self.rubber = obj.rubber
        self.id = obj.id
        self.revby = obj.revby
        self.revdate = obj.revdate
        self.valid = obj.valid

        return True


ORMClass: TypeAlias = (CARS
    |PEOPLE
    |TIRES)


def make_db(connection_string):
    engine = create_engine(connection_string, echo=True)
    Base.metadata.create_all(engine)