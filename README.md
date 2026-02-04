# ♟️ Archess — in-terminal chess game

A terminal-based chess game written in Python with self-made modular engine.

## 🚀 Getting Started

This project uses **uv** for fast dependency management and execution. To get the game running on your machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shinzo13/archess.git
   cd archess
   ```
2. **Run the game:**
   ```bash
   uv run python -m src
   ```
## 🕹 How to Play

Once the game starts, the colored board will render in your terminal.

* **Input Format**: Use coordinate-based moves. Type the starting square followed by the destination square (e.g., **e2e4** or **g1f3**).
* **Game Logic**: The engine automatically detects Check, Checkmate, and Stalemate.
* **Exit**: Type **quit** at any time to end the session.

## 🏗 Architecture Overview

The game logic is decoupled into specialized modules located in `src/core/utils/` to ensure high performance and easy debugging:

* **Position Manager**: Handles grid navigation and piece lookups.
* **Move Generator**: Calculates all pseudo-legal movement paths.
* **Move Validator**: Manages king safety and legal move filtering.

### Full project tree
```
src
├── __main__.py
├── core
│   ├── engine.py
│   ├── __init__.py
│   └── utils
│       ├── __init__.py
│       ├── move_generator.py
│       ├── move_validator.py
│       └── position_manager.py
├── models
│   ├── board.py
│   ├── enums
│   │   ├── __init__.py
│   │   ├── piece_type.py
│   │   ├── status.py
│   │   └── team.py
│   ├── __init__.py
│   └── piece.py
└── tui
    ├── screen.py
    └── utils
        └── parse_move.py
```

## 🛠 Requirements

* **Python 3.14+**
* **uv** packet manager
* **Terminal**: A terminal with TrueColor support (e.g., iTerm2, Windows Terminal, Kitty, or VS Code Terminal).

---

## 📄 License
This project is licensed under the MIT License.