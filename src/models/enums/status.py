from enum import StrEnum, auto

class Status(StrEnum):
    ACTIVE = auto()
    WHITE_WON = auto()
    BLACK_WON = auto()
    DRAW = auto()