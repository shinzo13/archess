from typing import Optional, List, Tuple

from src.models.board import Board
from src.models.enums.piece_type import PieceType
from src.models.enums.team import Team
from src.models.piece import Piece


class PositionManager:
    def __init__(self, board: Board):
        self.board = board

    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        if not self.is_valid_position(row, col):
            return None
        return self.board.grid[row][col]

    def is_empty(self, row: int, col: int) -> bool:
        return self.is_valid_position(row, col) and self.board.grid[row][col] is None

    def is_occupied_by_team(self, row: int, col: int, team: Team) -> bool:
        piece = self.get_piece(row, col)
        return piece is not None and piece.team == team

    def is_occupied_by_opponent(self, row: int, col: int, team: Team) -> bool:
        piece = self.get_piece(row, col)
        return piece is not None and piece.team != team

    def find_king(self, team: Team) -> Optional[Tuple[int, int]]:
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.type == PieceType.KING and piece.team == team:
                    return (row, col)
        return None

    def get_all_pieces(self, team: Team) -> List[Tuple[int, int, Piece]]:
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.team == team:
                    pieces.append((row, col, piece))
        return pieces
