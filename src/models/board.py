from typing import Optional, Tuple, List, Dict
from pydantic import BaseModel, Field

from src.models.enums.team import Team
from src.models.piece import Piece


class Board(BaseModel):
    # Use default_factory for mutable objects like lists and dicts
    grid: List[List[Optional[Piece]]] = Field(
        default_factory=lambda: [[None for _ in range(8)] for _ in range(8)]
    )

    captured_pieces: List[Piece] = Field(default_factory=list)

    en_passant_target: Optional[Tuple[int, int]] = None

    castling_rights: Dict[Team, Dict[str, bool]] = Field(
        default_factory=lambda: {
            Team.WHITE: {'kingside': True, 'queenside': True},
            Team.BLACK: {'kingside': True, 'queenside': True}
        }
    )

    # These were missing and causing your Traceback errors:
    halfmove_clock: int = 0
    fullmove_number: int = 1

    class Config:
        # This allows the model to handle the Team enum as keys in the dict
        use_enum_values = False
        arbitrary_types_allowed = True