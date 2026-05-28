"""
Точка входа в игру 2048.

Запускает игровой контроллер и начинает игровой цикл.
"""
from controllers.game_controller import GameController


def main():
    """Создает и запускает игру."""
    game = GameController()
    game.run()


if __name__ == "__main__":
    main()