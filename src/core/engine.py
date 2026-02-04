from src.core.utils import MoveValidator, MoveGenerator, PositionManager
from src.models import Board, Piece
from src.models.enums import Team, PieceType


class ChessEngine:
    def __init__(self, board: Board):
        self.board = board
        self.current_turn = Team.WHITE
        self.pos = PositionManager(board)
        self.gen = MoveGenerator(self.pos)
        self.val = MoveValidator(self.pos, self.gen)

    def setup_initial_position(self):
        self.board.grid[0][0] = Piece(type=PieceType.ROOK, team=Team.BLACK)
        self.board.grid[0][1] = Piece(type=PieceType.KNIGHT, team=Team.BLACK)
        self.board.grid[0][2] = Piece(type=PieceType.BISHOP, team=Team.BLACK)
        self.board.grid[0][3] = Piece(type=PieceType.QUEEN, team=Team.BLACK)
        self.board.grid[0][4] = Piece(type=PieceType.KING, team=Team.BLACK)
        self.board.grid[0][5] = Piece(type=PieceType.BISHOP, team=Team.BLACK)
        self.board.grid[0][6] = Piece(type=PieceType.KNIGHT, team=Team.BLACK)
        self.board.grid[0][7] = Piece(type=PieceType.ROOK, team=Team.BLACK)

        for col in range(8):
            self.board.grid[1][col] = Piece(type=PieceType.PAWN, team=Team.BLACK)

        for col in range(8):
            self.board.grid[6][col] = Piece(type=PieceType.PAWN, team=Team.WHITE)

        self.board.grid[7][0] = Piece(type=PieceType.ROOK, team=Team.WHITE)
        self.board.grid[7][1] = Piece(type=PieceType.KNIGHT, team=Team.WHITE)
        self.board.grid[7][2] = Piece(type=PieceType.BISHOP, team=Team.WHITE)
        self.board.grid[7][3] = Piece(type=PieceType.QUEEN, team=Team.WHITE)
        self.board.grid[7][4] = Piece(type=PieceType.KING, team=Team.WHITE)
        self.board.grid[7][5] = Piece(type=PieceType.BISHOP, team=Team.WHITE)
        self.board.grid[7][6] = Piece(type=PieceType.KNIGHT, team=Team.WHITE)
        self.board.grid[7][7] = Piece(type=PieceType.ROOK, team=Team.WHITE)

    def make_move(self, fr: int, fc: int, tr: int, tc: int) -> bool:
        piece = self.pos.get_piece(fr, fc)
        if not piece or piece.team != self.current_turn:
            return False

        if (tr, tc) not in self.val.get_legal_moves(fr, fc):
            return False

        captured = self.pos.get_piece(tr, tc)
        if captured:
            self.board.captured_pieces.append(captured)
            self.board.halfmove_clock = 0

        if piece.type == PieceType.PAWN:
            self.board.halfmove_clock = 0
        else:
            self.board.halfmove_clock += 1

        self.board.grid[tr][tc] = piece
        self.board.grid[fr][fc] = None
        piece.has_moved = True

        self.current_turn = Team.BLACK if self.current_turn == Team.WHITE else Team.WHITE
        if self.current_turn == Team.WHITE:
            self.board.fullmove_number += 1
        return True

    def get_board_string(self) -> str:
        BG1 = "160;100;100"
        BG2 = "190;150;140"
        WHITE_FG = "255;255;255"
        BLACK_FG = "0;0;0"
        RESET = "\033[0m"

        UNICODE_SYMBOLS = {
            PieceType.PAWN: '󰡙',
            PieceType.BISHOP: '󰡜',
            PieceType.KNIGHT: '󰡘',
            PieceType.ROOK: '󰡛',
            PieceType.QUEEN: '󰡚',
            PieceType.KING: '󰡗',
        }

        result = "\n    a  b  c  d  e  f  g  h\n"

        for row in range(8):
            line = f" {8 - row} "
            for col in range(8):
                piece = self.pos.get_piece(row, col)
                bg_color = BG1 if (row + col) % 2 == 0 else BG2
                cell_str = f"\033[48;2;{bg_color}m"
                if piece:
                    fg_color = WHITE_FG if piece.team == Team.WHITE else BLACK_FG
                    symbol = UNICODE_SYMBOLS[piece.type]
                    cell_str += f"\033[38;2;{fg_color}m {symbol} "
                else:
                    cell_str += "   "
                line += cell_str + RESET
            result += line + f" {8 - row}\n"
        result += "    a  b  c  d  e  f  g  h\n"
        return result