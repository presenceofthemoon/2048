#сборная солянка 

# Окно
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "2048 Game"

# Сетка
GRID_SIZE = 4
CELL_SIZE = 100
GRID_PADDING = 10
GRID_OFFSET_X = (SCREEN_WIDTH - (GRID_SIZE * CELL_SIZE + (GRID_SIZE + 1) * GRID_PADDING)) // 2
GRID_OFFSET_Y = 150

# Цвета
BACKGROUND_COLOR = (250, 248, 239)
GRID_COLOR = (205, 193, 180)
EMPTY_CELL_COLOR = (238, 228, 218)

# Цвета плиток
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Цвет текста
TEXT_COLOR_LIGHT = (119, 110, 101)
TEXT_COLOR_DARK = (249, 246, 242)

# Шрифт
FONT_SIZE = 40
FONT_SIZE_SMALL = 25


SAVE_FILE = "save.json"

# Настройки звука
SOUND_ENABLED = True
MUSIC_ENABLED = True
SOUND_VOLUME = 0.3
MUSIC_VOLUME = 0.5

# Пути к аудио файлам
SOUNDS_DIR = "assets/sounds"
MUSIC_FILE = f"{SOUNDS_DIR}/background_music.mp3"
SOUND_MOVE = f"{SOUNDS_DIR}/move.wav"
SOUND_MERGE = f"{SOUNDS_DIR}/merge.wav"
SOUND_WIN = f"{SOUNDS_DIR}/win.wav"
SOUND_GAMEOVER = f"{SOUNDS_DIR}/gameover.wav"