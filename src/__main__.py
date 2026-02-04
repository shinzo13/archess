from src.models.board import Board
from src.core import ChessEngine
from src.models.enums.team import Team
from src.tui.screen import ScreenManager
from src.tui.utils.parse_move import parse_move


def main():
    board = Board()
    engine = ChessEngine(board)
    engine.setup_initial_position()

    screen = ScreenManager()

    game_over = False
    message = "Welcome to Archess!! Enter moves like 'e2e4' or 'quit'."

    while True:
        if not screen.check_screen_size():
            continue
        screen.render_board(engine, message)
        if game_over:
            break

        user_input = screen.render_input()

        if user_input == 'quit':
            print("Thanks for playing! Bye!!!!!")
            break

        move_coords = parse_move(user_input)

        if move_coords:
            (fr, fc), (tr, tc) = move_coords
            success = engine.make_move(fr, fc, tr, tc)

            if success:
                message = f"Last move: {user_input}"

                if engine.val.is_checkmate(engine.current_turn):
                    winner = "BLACK" if engine.current_turn == Team.WHITE else "WHITE"
                    message = f"CHECKMATE! {winner} wins!"
                    game_over = True
                elif engine.val.is_in_check(engine.current_turn):
                    message += " - CHECK!"
            else:
                message = "Invalid move!"
        else:
            message = "Invalid format! Valid format: 'e2e4'."


if __name__ == "__main__":
    main()