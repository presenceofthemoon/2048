# 2048 Game

A Python implementation of the popular 2048 puzzle game using Pygame. Slide numbered tiles on a grid to combine them and reach the 2048 tile!

## About

This is my take on the classic 2048 game. I built it to practice Python and learn game development with Pygame. The game follows the original rules - use arrow keys to slide tiles, combine matching numbers, and try to reach 2048 (or go even higher if you're up for the challenge).

## Features

- Clean MVC architecture for maintainable code
- Smooth gameplay with Pygame
- Score tracking
- Save/load game functionality
- Win/lose detection
- Auto-save on exit

## Getting Started

### Requirements

- Python 3.8 or higher
- Pygame 2.5.0+

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/2048.git
cd 2048
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### How to Play

Run the game:
```bash
python main.py
```

**Controls:**
- Arrow Keys - Move tiles
- ESC - Quit game
- R - Restart game

**Rules:**
- Use arrow keys to slide all tiles in one direction
- When two tiles with the same number touch, they merge into one
- After each move, a new tile (2 or 4) appears in a random empty spot
- The game ends when you can't make any more moves
- Reach 2048 to win (but you can keep playing to get an even higher score!)

## Project Structure

```
2048/
├── models/          # Game logic and data models
│   ├── game.py      # Core game mechanics
│   └── tile.py      # Tile class
├── views/           # UI rendering
│   ├── game_view.py # Game board visualization
│   └── menu_view.py # Menu interface
├── controllers/     # Game flow control
│   └── game_controller.py
├── utils/           # Helper utilities
│   └── save_manager.py
├── tests/           # Unit tests
│   └── test_game.py
├── main.py          # Entry point
└── requirements.txt # Dependencies
```

## Development

The codebase uses a Model-View-Controller pattern to keep things organized:
- **Models** handle game state and logic
- **Views** take care of rendering
- **Controllers** manage user input and game flow

### Running Tests

```bash
python -m pytest tests/
```

## License

Feel free to use this code for learning or your own projects.

## Acknowledgments

Based on the original [2048 game](https://github.com/gabrielecirulli/2048) by Gabriele Cirulli.
