from typing import List, Tuple

from src.core.utils import PositionManager, MoveGenerator
from src.models.enums import Team


class MoveValidator:
    def __init__(self, pos: 'PositionManager', gen: 'MoveGenerator'):
        self.pos = pos
        self.gen = gen

    def is_in_check(self, team: Team) -> bool:
        king_pos = self.pos.find_king(team)
        if not king_pos: return False

        opponent = Team.BLACK if team == Team.WHITE else Team.WHITE
        for r, c, piece in self.pos.get_all_pieces(opponent):
            if king_pos in self.gen.get_pseudo_legal_moves(r, c):
                return True
        return False

    def get_legal_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        piece = self.pos.get_piece(row, col)
        if not piece: return []

        pseudo = self.gen.get_pseudo_legal_moves(row, col)
        legal = []
        for tr, tc in pseudo:
            if not self._would_be_in_check(row, col, tr, tc, piece.team):
                legal.append((tr, tc))
        return legal

    def _would_be_in_check(self, fr, fc, tr, tc, team) -> bool:
        # Симуляция
        orig = self.pos.board.grid[tr][tc]
        moving = self.pos.board.grid[fr][fc]
        self.pos.board.grid[tr][tc] = moving
        self.pos.board.grid[fr][fc] = None

        in_check = self.is_in_check(team)

        # Откат
        self.pos.board.grid[fr][fc] = moving
        self.pos.board.grid[tr][tc] = orig
        return in_check

    def is_checkmate(self, team: Team) -> bool:
        if not self.is_in_check(team): return False
        return not any(self.get_legal_moves(r, c) for r, c, p in self.pos.get_all_pieces(team))

    def is_stalemate(self, team: Team) -> bool:
        if self.is_in_check(team): return False
        return not any(self.get_legal_moves(r, c) for r, c, p in self.pos.get_all_pieces(team))
