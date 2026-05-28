"""
Менеджер сохранений игры.

Отвечает за сохранение и загрузку состояния игры в файл,
чтобы игрок мог продолжить игру после выхода.
"""
import json
import os
from models.game import Game2048
from config import SAVE_FILE


class SaveManager:
    """
    Управляет сохранением и загрузкой игры.
    
    Сериализует состояние игры в JSON и сохраняет в файл.
    Позволяет игроку продолжить игру с того места, где остановился.
    """
    
    def __init__(self):
        """
        Инициализирует менеджер сохранений.
        
        Создает путь к файлу сохранения из конфига.
        """
        self.save_path = SAVE_FILE
    
    def save(self, game: Game2048) -> bool:
        try:
            data = {
                'grid': game.get_grid_values(),
                'score': game.score,
            }
            with open(self.save_path, 'w') as f:
                json.dump(data, f)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False
    
    def load(self, game: Game2048) -> bool:
        if not os.path.exists(self.save_path):
            return False
        
        try:
            with open(self.save_path, 'r') as f:
                data = json.load(f)
            
            game.load_grid(data['grid'], data['score'])
            return True
        except Exception as e:
            print(f"Error loading game: {e}")
            return False
    
    def delete(self) -> bool:
        if os.path.exists(self.save_path):
            os.remove(self.save_path)
            return True
        return False