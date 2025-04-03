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

    def possible_move(self, targetpos, intialpos, piece):
        targetX, targetY = targetpos
        initialX, initialY = intialpos
        if(self.squares[targetX][targetY].blank() == False):
            if(self.squares[targetX][targetY].piece.color == piece.color):
                return False
        
        moves = self.get_moves(intialpos, piece)
        for k in moves:
            print(k)
            if(targetX == k[0] and targetY == k[1]):
                piece.moved = True
                return True
        return False
    
    def get_moves(self, intialpos, piece):
        res = []
        initialX, initialY = intialpos
        if(piece.name == 'pawn'):
            x = initialX + piece.dir
            y = initialY
            print("-", x, " ", y)
            if (0 <= x) and (x < ROWS) and (0 <= y) and (y < COLS) and self.squares[x][y].blank() == True: 
                print("hello",self.squares[x][y].blank())
                res.append((x, y))

            if(piece.moved == False):
                x = initialX + piece.dir * 2
                y = initialY
                print("-", x, " ", y)
                if (0 <= x) and (x < ROWS) and (0 <= y) and (y < COLS) and self.squares[x][y].blank() == True: 
                    res.append((x, y))      

            x = initialX + piece.dir
            y = initialY + 1
            print("-", x, " ", y)
            if (0 <= x) and (x < ROWS) and (0 <= y) and (y < COLS): 
                if self.squares[x][y].blank() == False and self.squares[x][y].piece.color != piece.color:
                    res.append((x, y))
            
            x = initialX + piece.dir
            y = initialY - 1
            print("-", x, " ", y)
            if (0 <= x) and (x < ROWS) and (0 <= y) and (y < COLS): 
                if self.squares[x][y].blank() == False and self.squares[x][y].piece.color != piece.color:
                    res.append((x, y))

        if(piece.name == 'rook') or (piece.name == 'queen'):
            x = initialX
            y = initialY
            while(x + 1 < ROWS):
                x = x + 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break
            
            x = initialX
            y = initialY
            while(x - 1 >= 0):
                x = x - 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break

            x = initialX
            y = initialY
            while(y + 1 < COLS):
                y = y + 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break

            x = initialX
            y = initialY
            while(y - 1 >= 0):
                y = y - 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break

        if(piece.name == 'knight'):
            for i in [-2, 2]:
                for j in [-1, 1]:
                    x = initialX + i
                    y = initialY + j
                    if (0 <= x) and (x < ROWS) and (0 <= y) and (y < COLS):
                        res.append((x, y))
            for i in [-1, 1]:
                for j in [-2, 2]:
                    x = initialX + i
                    y = initialY + j
                    if (0 <= x) and (x < ROWS) and (0 <= y) and (y < COLS):
                        res.append((x, y))

        if(piece.name == 'bishop') or (piece.name == 'queen'):
            x = initialX
            y = initialY
            while(x + 1 < ROWS) and (y + 1 < COLS):
                x = x + 1
                y = y + 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break

            x = initialX
            y = initialY
            while(x - 1 >= 0) and (y - 1 >= 0):
                x = x - 1
                y = y - 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break
                    
            x = initialX
            y = initialY
            while(x + 1 < ROWS) and (y - 1 >= 0):
                x = x + 1
                y = y - 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break

            x = initialX
            y = initialY
            while(x - 1 >= 0) and (y + 1 < COLS):
                x = x - 1
                y = y + 1
                res.append((x, y))
                if(self.squares[x][y].blank() == False):
                    break
        if(piece.name == 'king'):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if(i != initialX) and (j != initialY):
                        res.append((initialX + i, initialY + j))
        
        return res
            


