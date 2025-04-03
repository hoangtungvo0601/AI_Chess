import os

class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        self.value = value
        if(color == 'white'):
            self.value = (-1) * self.value
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.moves = []
        self.moved = False

    def set_texture(self, size=80):
        self.texture = os.path.join(
            "assets", "images", f"imgs-{size}px", f"{self.color}_{self.name}.png"
        )
        if not os.path.exists(self.texture):
            print(f"Error: File not found - {self.texture}")


    def add_move(self, move):
        self.moves.append(move)
        moved = True


class Pawn(Piece):
    def __init__(self, color):
        self.dir = 1
        if(color == 'white'):
            self.dir = -1
        
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color): 
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color): 
        super().__init__('bishop', color, 3.0)

class Rook(Piece):
    def __init__(self, color): 
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color): 
        super().__init__('queen', color, 9.0)
    
class King(Piece):
    def __init__(self, color): 
        super().__init__('king', color, 100000.0)

