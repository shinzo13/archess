import os
import shutil

from src.core import ChessEngine


class ScreenManager:
    def __init__(self):
        pass

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_screen_size(self):
        if shutil.get_terminal_size().columns > 65:
            self._clear_screen()
            print("Please, make your screen content size bigger so you can play Archess!")
            return False
        return True

    def render_board(self, engine: ChessEngine, message: str):
        self._clear_screen()
        print("\n" + engine.get_board_string() + "\n")
        print(f"Current Turn: {engine.current_turn.name}")
        print(f"Status: {message}")

    def render_input(self):
        print("-" * 20)
        return input("Enter move: ").strip().lower()