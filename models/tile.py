

class Tile:
    
    def __init__(self, value: int = 2, x: int = 0, y: int = 0):
        self.value = value
        self.x = x
        self.y = y
        self.merged = False
    
    def double(self):
        self.value *= 2
        self.merged = True
    
    def reset_merged(self):
        self.merged = False
    
    def __repr__(self):
        return f"Tile({self.value})"