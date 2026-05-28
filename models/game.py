"""
Основная игровая логика 2048.

Этот модуль содержит класс Game2048, который управляет всей механикой игры:
движением плиток, их объединением, подсчетом очков и определением конца игры.
"""
import random
from typing import List, Optional, Tuple
from models.tile import Tile


class Game2048:
    """
    Основной класс игры 2048.
    
    Управляет игровым полем 4x4, логикой движения плиток, их объединением,
    подсчетом очков и определением состояния игры (выигрыш/проигрыш).
    """
    
    def __init__(self, size: int = 4):
        """
        Инициализирует новую игру.
        
        Args:
            size: Размер игрового поля (по умолчанию 4x4)
        """
        self.size = size
        self.grid: List[List[Optional[Tile]]] = [[None] * size for _ in range(size)]
        self.score = 0
        self.game_over = False
        self.won = False
        self._initialize_game()
    
    def _initialize_game(self):
        self.add_random_tile()
        self.add_random_tile()
    
    def add_random_tile(self) -> bool:
        empty_cells = self._get_empty_cells()
        if not empty_cells:
            return False
        
        x, y = random.choice(empty_cells)
        value = 4 if random.random() < 0.1 else 2
        self.grid[y][x] = Tile(value, x, y)
        return True
    
    def _get_empty_cells(self) -> List[Tuple[int, int]]:
        return [(x, y) for y in range(self.size) 
                for x in range(self.size) if self.grid[y][x] is None]
    
    def move(self, direction: str) -> bool:
        if self.game_over:
            return False
        
        self._reset_merged_flags()
        
        moved = False
        
        if direction == 'left':
            moved = self._move_left()
        elif direction == 'right':
            moved = self._move_right()
        elif direction == 'up':
            moved = self._move_up()
        elif direction == 'down':
            moved = self._move_down()
        
        if moved:
            self.add_random_tile()
            self._check_game_state()
        
        return moved
    
    def _reset_merged_flags(self):
        for row in self.grid:
            for tile in row:
                if tile:
                    tile.reset_merged()
    
    def _move_left(self) -> bool:
        moved = False
        for y in range(self.size):
            row = [tile for tile in self.grid[y] if tile is not None]
            new_row = self._merge_row(row)
            
            while len(new_row) < self.size:
                new_row.append(None)
            
            for x, tile in enumerate(new_row):
                if tile:
                    tile.x = x
                    tile.y = y
            
            if self._row_changed(self.grid[y], new_row):
                moved = True
            
            self.grid[y] = new_row
        
        return moved
    
    def _move_right(self) -> bool:
        moved = False
        for y in range(self.size):
            row = [tile for tile in self.grid[y] if tile is not None]
            new_row = self._merge_row(row[::-1])[::-1]
            
            while len(new_row) < self.size:
                new_row.insert(0, None)
            
            for x, tile in enumerate(new_row):
                if tile:
                    tile.x = x
                    tile.y = y
            
            if self._row_changed(self.grid[y], new_row):
                moved = True
            
            self.grid[y] = new_row
        
        return moved
    
    def _move_up(self) -> bool:
        moved = False
        for x in range(self.size):
            col = [self.grid[y][x] for y in range(self.size) if self.grid[y][x] is not None]
            new_col = self._merge_row(col)
            
            while len(new_col) < self.size:
                new_col.append(None)
            
            for y, tile in enumerate(new_col):
                if tile:
                    tile.x = x
                    tile.y = y
            
            old_col = [self.grid[y][x] for y in range(self.size)]
            if self._row_changed(old_col, new_col):
                moved = True
            
            for y in range(self.size):
                self.grid[y][x] = new_col[y]
        
        return moved
    
    def _move_down(self) -> bool:
        moved = False
        for x in range(self.size):
            col = [self.grid[y][x] for y in range(self.size) if self.grid[y][x] is not None]
            new_col = self._merge_row(col[::-1])[::-1]
            
            while len(new_col) < self.size:
                new_col.insert(0, None)
            
            for y, tile in enumerate(new_col):
                if tile:
                    tile.x = x
                    tile.y = y
            
            old_col = [self.grid[y][x] for y in range(self.size)]
            if self._row_changed(old_col, new_col):
                moved = True
            
            for y in range(self.size):
                self.grid[y][x] = new_col[y]
        
        return moved
    
    def _merge_row(self, row: List[Tile]) -> List[Tile]:
        if not row:
            return []
        
        merged_row = []
        skip = False
        
        for i in range(len(row)):
            if skip:
                skip = False
                continue
            
            if i + 1 < len(row) and row[i].value == row[i + 1].value:
                new_tile = Tile(row[i].value * 2, row[i].x, row[i].y)
                new_tile.merged = True
                merged_row.append(new_tile)
                self.score += new_tile.value
                
                if new_tile.value == 2048:
                    self.won = True
                
                skip = True
            else:
                merged_row.append(row[i])
        
        return merged_row
    
    def _row_changed(self, old_row: List[Optional[Tile]], new_row: List[Optional[Tile]]) -> bool:
        if len(old_row) != len(new_row):
            return True
        
        for old, new in zip(old_row, new_row):
            if old is None and new is not None:
                return True
            if old is not None and new is None:
                return True
            if old is not None and new is not None and old.value != new.value:
                return True
        
        return False
    
    def _check_game_state(self):
        
        if self._get_empty_cells():
            return
        
        for y in range(self.size):
            for x in range(self.size):
                tile = self.grid[y][x]
                if not tile:
                    continue
                
                if x < self.size - 1 and self.grid[y][x + 1] and \
                   self.grid[y][x + 1].value == tile.value:
                    return
                
                if y < self.size - 1 and self.grid[y + 1][x] and \
                   self.grid[y + 1][x].value == tile.value:
                    return
        
        self.game_over = True
    
    def get_grid_values(self) -> List[List[int]]:
        return [[tile.value if tile else 0 for tile in row] for row in self.grid]
    
    def load_grid(self, grid_values: List[List[int]], score: int):
        self.grid = [[None] * self.size for _ in range(self.size)]
        for y in range(self.size):
            for x in range(self.size):
                if grid_values[y][x] != 0:
                    self.grid[y][x] = Tile(grid_values[y][x], x, y)
        self.score = score
        self.game_over = False
        self.won = False
    
    def restart(self):
        self.grid = [[None] * self.size for _ in range(self.size)]
        self.score = 0
        self.game_over = False
        self.won = False
        self._initialize_game()