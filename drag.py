import pygame

class Drag:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self, surface):
        if self.piece == None:
            return
        # texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # img
        img = pygame.image.load(texture)
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
    
    def save_pos(self, row, col):
        self.initial_row = row
        self.initial_col = col

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False