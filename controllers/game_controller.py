import pygame
from models.game import Game2048
from views.game_view import GameView
from views.menu_view import MenuView
from utils.save_manager import SaveManager
from config import *


class GameController:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        self.game = Game2048()
        self.game_view = GameView(self.screen)
        self.menu_view = MenuView(self.screen)
        self.save_manager = SaveManager()
        
        self.running = True
        self.in_game = False
        self.paused = False
    
    def run(self):
        while self.running:
            if not self.in_game:
                self._handle_menu()
            else:
                self._handle_game()
            
            self.clock.tick(FPS)
        
        pygame.quit()
    
    def _handle_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                buttons = [
                    ("New Game", "new_game", 250),
                    ("Continue", "continue", 320),
                    ("Quit", "quit", 390),
                ]
                
                for text, action, y_pos in buttons:
                    button_rect = pygame.Rect(125, y_pos, 200, 50)
                    
                    if button_rect.collidepoint(mouse_pos):
                        if action == 'new_game':
                            self.game.restart()
                            self.in_game = True
                            self.paused = False
                        elif action == 'continue':
                            if self.save_manager.load(self.game):
                                self.in_game = True
                                self.paused = False
                        elif action == 'quit':
                            self.running = False
                        break
        
        self.menu_view.draw_main_menu()
        pygame.display.flip()
    
    def _handle_game(self):
        self.game_view.draw(self.game)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._handle_pause()
                
                elif event.key == pygame.K_r and self.game.game_over:
                    self.game.restart()
                
                elif event.key == pygame.K_c and self.game.won:
                    self.game.won = False
                
                elif not self.paused and not self.game.game_over:
                    direction = None
                    
                    if event.key == pygame.K_LEFT:
                        direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        direction = 'right'
                    elif event.key == pygame.K_UP:
                        direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        direction = 'down'
                    
                    if direction:
                        self.game.move(direction)
    
    def _handle_pause(self):
        self.paused = True
        
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.paused = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    buttons = [
                        ("Resume", "resume", 280),
                        ("Restart", "restart", 350),
                        ("Main Menu", "menu", 420),
                    ]
                    
                    for text, action, y_pos in buttons:
                        button_rect = pygame.Rect(125, y_pos, 200, 50)
                        
                        if button_rect.collidepoint(mouse_pos):
                            if action == 'resume':
                                self.paused = False
                            elif action == 'restart':
                                self.game.restart()
                                self.paused = False
                            elif action == 'menu':
                                self.save_manager.save(self.game)
                                self.in_game = False
                                self.paused = False
                            break
            
            self.menu_view.draw_pause_menu()
            pygame.display.flip()