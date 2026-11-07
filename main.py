"""Точка входа в игру"""
from controllers.game_controller import GameController


def main():
    """Запуск игры"""
    game = GameController()
    game.run()


if __name__ == "__main__":
    main()