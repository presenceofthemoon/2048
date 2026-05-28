import unittest
from models.game import Game2048
from models.tile import Tile


class TestTile(unittest.TestCase):
    
    def test_tile_creation(self):
        tile = Tile(2, 0, 0)
        self.assertEqual(tile.value, 2)
        self.assertFalse(tile.merged)
    
    def test_tile_double(self):
        tile = Tile(2)
        tile.double()
        self.assertEqual(tile.value, 4)
        self.assertTrue(tile.merged)


class TestGame2048(unittest.TestCase):
    
    def setUp(self):
        self.game = Game2048(4)
    
    def test_initialization(self):
        self.assertEqual(len(self.game.grid), 4)
        self.assertEqual(len(self.game.grid[0]), 4)
        self.assertEqual(self.game.score, 0)
        self.assertFalse(self.game.game_over)
    
    def test_add_random_tile(self):
        game = Game2048(2)
        game.grid = [[None, None], [None, None]]
        
        result = game.add_random_tile()
        self.assertTrue(result)
        
        tiles_count = sum(1 for row in game.grid for tile in row if tile is not None)
        self.assertEqual(tiles_count, 1)
    
    def test_move_left(self):
        game = Game2048(2)
        game.grid = [
            [Tile(2), Tile(2)],
            [None, None]
        ]
        
        moved = game.move('left')
        self.assertTrue(moved)
        self.assertEqual(game.grid[0][0].value, 4)
        self.assertIsNone(game.grid[0][1])
    
    def test_merge_tiles(self):
        game = Game2048(2)
        game.grid = [
            [Tile(2), Tile(2), Tile(2), Tile(2)],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ]
        
        game.move('left')
        self.assertEqual(game.grid[0][0].value, 4)
        self.assertEqual(game.grid[0][1].value, 4)
    
    def test_score_increases(self):
        game = Game2048(2)
        game.grid = [
            [Tile(2), Tile(2)],
            [None, None]
        ]
        
        initial_score = game.score
        game.move('left')
        self.assertEqual(game.score, initial_score + 4)
    
    def test_grid_values(self):
        game = Game2048(2)
        game.grid = [
            [Tile(2), None],
            [None, Tile(4)]
        ]
        
        values = game.get_grid_values()
        self.assertEqual(values, [[2, 0], [0, 4]])


if __name__ == '__main__':
    unittest.main()