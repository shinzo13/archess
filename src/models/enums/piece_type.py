from enum import StrEnum, auto

class PieceType(StrEnum):
    PAWN = auto()
    KING = auto()
    QUEEN = auto()
    KNIGHT = auto()
    ROOK = auto()
    BISHOP = auto()