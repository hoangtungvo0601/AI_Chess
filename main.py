from const import *
from game import *

import pygame
import sys

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game()
        pygame.display.set_caption("Chess")

    def mainloop(self):
        while True:
            self.game.show_bg(self.screen)
            self.game.show_pc(self.screen)
            drag = self.game.drag
            drag.update_blit(self.screen)
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    drag.update_mouse(event.pos)
                    choosen_row = drag.mouseY // SQSIZE
                    choosen_col = drag.mouseX // SQSIZE
                    print(drag.mouseX, choosen_row)
                    print(drag.mouseY, choosen_col)
                    print(self.game.board.squares[choosen_row][choosen_col].piece)
                    if(self.game.board.squares[choosen_row][choosen_col].blank() == False): 
                        drag.save_pos(choosen_row, choosen_col)
                        drag.drag_piece(self.game.board.squares[choosen_row][choosen_col].piece)

                elif event.type == pygame.MOUSEMOTION:
                    if(drag.dragging == True):
                        drag.update_mouse(event.pos)
                        drag.update_blit(self.screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                        if(drag.dragging == True):
                            piece = drag.piece
                            piece.set_texture(size=80)
                            drag.update_mouse(event.pos)
                            choosen_row = drag.mouseY // SQSIZE
                            choosen_col = drag.mouseX // SQSIZE
                            if(self.game.board.squares[choosen_row][choosen_col].blank() == True):
                                self.game.board.squares[choosen_row][choosen_col].piece = piece
                                self.game.board.squares[drag.initial_row][drag.initial_col].piece = None
                                
                            drag.undrag_piece()
                elif(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()


            pygame.display.update()
    
main = Main()
main.mainloop()