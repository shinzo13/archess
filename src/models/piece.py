from pydantic import BaseModel

from src.models.enums.piece_type import PieceType
from src.models.enums.team import Team


class Piece(BaseModel):
    type: PieceType
    team: Team
    has_moved: bool = False
