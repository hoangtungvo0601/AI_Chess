from square import *
from const import *
from piece import *

class Board:
    def __init__(self):
        self.squares = []
        self._createSquares()
        self._addPieces()

    def _createSquares(self):
        for i in range(ROWS):
            nrow = []
            for j in range(COLS):
                nrow.append(Square(i, j))
            self.squares.append(nrow)

    def _addPieces(self):
        for i in range(COLS):
            self.squares[1][i] = Square(1, i, Pawn('black'))
            self.squares[6][i] = Square(6, i, Pawn('white'))
            if(i == 0) or (i == 7):
                self.squares[0][i] = Square(0, i, Rook('black'))
                self.squares[7][i] = Square(7, i, Rook('white'))
            if(i == 1) or (i == 6):
                self.squares[0][i] = Square(0, i, Knight('black'))
                self.squares[7][i] = Square(7, i, Knight('white'))
            if(i == 2) or (i == 5):
                self.squares[0][i] = Square(0, i, Bishop('black'))
                self.squares[7][i] = Square(7, i, Bishop('white'))
            if(i == 3):
                self.squares[0][i] = Square(0, i, Queen('black'))
                self.squares[7][i] = Square(7, i, King('white'))
            if(i == 4):
                self.squares[0][i] = Square(0, i, King('black'))
                self.squares[7][i] = Square(7, i, Queen('white'))

