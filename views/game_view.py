import pygame
from config import *
from models.game import Game2048


class GameView:
    
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_large = pygame.font.Font(None, FONT_SIZE)
        self.font_small = pygame.font.Font(None, FONT_SIZE_SMALL)
        self.font_score = pygame.font.Font(None, 35)
    
    def draw(self, game: Game2048):
        self.screen.fill(BACKGROUND_COLOR)
        self._draw_header(game)
        self._draw_grid()
        self._draw_tiles(game)
        
        if game.game_over:
            self._draw_game_over()
        elif game.won:
            self._draw_won()
    
    def _draw_header(self, game: Game2048):
        title = self.font_large.render("2048", True, TEXT_COLOR_LIGHT)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 60))
        self.screen.blit(title, title_rect)
        
        score_text = self.font_score.render(f"Score: {game.score}", True, TEXT_COLOR_LIGHT)
        self.screen.blit(score_text, (20, 100))
        
        hint = self.font_small.render("Use arrow keys", True, TEXT_COLOR_LIGHT)
        hint_rect = hint.get_rect(center=(SCREEN_WIDTH // 2, 130))
        self.screen.blit(hint, hint_rect)
    
    def _draw_grid(self):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = self._get_cell_rect(x, y)
                pygame.draw.rect(self.screen, EMPTY_CELL_COLOR, rect, border_radius=5)
    
    def _draw_tiles(self, game: Game2048):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                tile = game.grid[y][x]
                if tile:
                    self._draw_tile(tile)
    
    def _draw_tile(self, tile):
        rect = self._get_cell_rect(tile.x, tile.y)
        color = TILE_COLORS.get(tile.value, (237, 194, 46))
        
        pygame.draw.rect(self.screen, color, rect, border_radius=5)
        
        text_color = TEXT_COLOR_LIGHT if tile.value <= 4 else TEXT_COLOR_DARK
        font = self.font_large if tile.value < 100 else self.font_small
        text = font.render(str(tile.value), True, text_color)
        text_rect = text.get_rect(center=rect.center)
        self.screen.blit(text, text_rect)
    
    def _get_cell_rect(self, x: int, y: int) -> pygame.Rect:
        left = GRID_OFFSET_X + GRID_PADDING + x * (CELL_SIZE + GRID_PADDING)
        top = GRID_OFFSET_Y + GRID_PADDING + y * (CELL_SIZE + GRID_PADDING)
        return pygame.Rect(left, top, CELL_SIZE, CELL_SIZE)
    
    def _draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BACKGROUND_COLOR)
        self.screen.blit(overlay, (0, 0))
        
        text = self.font_large.render("Game Over!", True, TEXT_COLOR_LIGHT)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        
        restart_text = self.font_small.render("Press R to restart", True, TEXT_COLOR_LIGHT)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)
    
    def _draw_won(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BACKGROUND_COLOR)
        self.screen.blit(overlay, (0, 0))
        
        text = self.font_large.render("You Win!", True, (237, 194, 46))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        
        continue_text = self.font_small.render("Press C to continue", True, TEXT_COLOR_LIGHT)
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(continue_text, continue_rect)