from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Status_Code(Enum):
    OK = 0
    INPUT_DOES_NOT_EXIST = 1
    OVERWRITE_INPUT = 2
    CHANGES_NOT_ACCEPTED = 3


@dataclass
class Status_Result:
    status_code: Status_Code = field()
    payload: Any = field()
    message: str = field(init=False)
