import pygame
from config import *


class MenuView:
    
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 60)
        self.font_medium = pygame.font.Font(None, 40)
        self.font_small = pygame.font.Font(None, 30)
    
    def draw_main_menu(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        title = self.font_large.render("2048", True, TEXT_COLOR_LIGHT)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        buttons = [
            ("New Game", 250),
            ("Continue", 320),
            ("Quit", 390),
        ]
        
        mouse_pos = pygame.mouse.get_pos()
        
        for text, y_pos in buttons:
            button_rect = pygame.Rect(125, y_pos, 200, 50)
            
            if button_rect.collidepoint(mouse_pos):
                color = (237, 194, 46)
            else:
                color = GRID_COLOR
            
            pygame.draw.rect(self.screen, color, button_rect, border_radius=10)
            
            text_surface = self.font_medium.render(text, True, TEXT_COLOR_LIGHT)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)
    
    def draw_pause_menu(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BACKGROUND_COLOR)
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_medium.render("Paused", True, TEXT_COLOR_LIGHT)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(title, title_rect)
        
        buttons = [
            ("Resume", 280),
            ("Restart", 350),
            ("Main Menu", 420),
        ]
        
        mouse_pos = pygame.mouse.get_pos()
        
        for text, y_pos in buttons:
            button_rect = pygame.Rect(125, y_pos, 200, 50)
            
            if button_rect.collidepoint(mouse_pos):
                color = (237, 194, 46)
            else:
                color = GRID_COLOR
            
            pygame.draw.rect(self.screen, color, button_rect, border_radius=10)
            
            text_surface = self.font_small.render(text, True, TEXT_COLOR_LIGHT)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)