from typing import List, Tuple

from src.core.utils import PositionManager
from src.models.enums.piece_type import PieceType
from src.models.enums.team import Team
from src.models.piece import Piece


class MoveGenerator:
    def __init__(self, pos: 'PositionManager'):
        self.pos = pos

    def get_pseudo_legal_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        piece = self.pos.get_piece(row, col)
        if not piece:
            return []

        if piece.type == PieceType.PAWN:
            return self._get_pawn_moves(row, col, piece)
        elif piece.type == PieceType.KNIGHT:
            return self._get_knight_moves(row, col, piece)
        elif piece.type == PieceType.BISHOP:
            return self._get_sliding_moves(row, col, piece, [(-1, -1), (-1, 1), (1, -1), (1, 1)])
        elif piece.type == PieceType.ROOK:
            return self._get_sliding_moves(row, col, piece, [(-1, 0), (1, 0), (0, -1), (0, 1)])
        elif piece.type == PieceType.QUEEN:
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            return self._get_sliding_moves(row, col, piece, directions)
        elif piece.type == PieceType.KING:
            return self._get_king_moves(row, col, piece)
        return []

    def _get_pawn_moves(self, row: int, col: int, piece: Piece) -> List[Tuple[int, int]]:
        moves = []
        direction = -1 if piece.team == Team.WHITE else 1
        start_row = 6 if piece.team == Team.WHITE else 1

        # Вперед
        if self.pos.is_empty(row + direction, col):
            moves.append((row + direction, col))
            if row == start_row and self.pos.is_empty(row + 2 * direction, col):
                moves.append((row + 2 * direction, col))

        # Взятия
        for dc in [-1, 1]:
            nr, nc = row + direction, col + dc
            if self.pos.is_occupied_by_opponent(nr, nc, piece.team):
                moves.append((nr, nc))
            elif self.pos.board.en_passant_target == (nr, nc):
                moves.append((nr, nc))
        return moves

    def _get_knight_moves(self, row, col, piece) -> List[Tuple[int, int]]:
        offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        moves = []
        for dr, dc in offsets:
            nr, nc = row + dr, col + dc
            if self.pos.is_valid_position(nr, nc):
                if self.pos.is_empty(nr, nc) or self.pos.is_occupied_by_opponent(nr, nc, piece.team):
                    moves.append((nr, nc))
        return moves

    def _get_sliding_moves(self, row, col, piece, directions) -> List[Tuple[int, int]]:
        moves = []
        for dr, dc in directions:
            curr_r, curr_c = row + dr, col + dc
            while self.pos.is_valid_position(curr_r, curr_c):
                if self.pos.is_empty(curr_r, curr_c):
                    moves.append((curr_r, curr_c))
                elif self.pos.is_occupied_by_opponent(curr_r, curr_c, piece.team):
                    moves.append((curr_r, curr_c))
                    break
                else:
                    break
                curr_r, curr_c = curr_r + dr, curr_c + dc
        return moves

    def _get_king_moves(self, row, col, piece) -> List[Tuple[int, int]]:
        moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0: continue
                nr, nc = row + dr, col + dc
                if self.pos.is_valid_position(nr, nc):
                    if self.pos.is_empty(nr, nc) or self.pos.is_occupied_by_opponent(nr, nc, piece.team):
                        moves.append((nr, nc))
        return moves
