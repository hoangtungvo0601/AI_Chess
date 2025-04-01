import pygame

from const import *
from board import *
from drag import *

class Game:
    def __init__(self):
        self.board = Board()
        self.drag = Drag()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if((row + col) % 2 == 0):
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rec = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rec)
    
    def show_pc(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (self.board.squares[row][col].blank() == False):
                    piece = self.board.squares[row][col].piece

                    if(piece is not self.drag.piece):
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE/2, row * SQSIZE + SQSIZE/2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)