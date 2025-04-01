class Square:
    def __init__(self, row, col, piece = None):
        self.col = col
        self.row = row
        self.piece = piece
    
    def blank(self):
        if(self.piece == None):
            return True
        else: 
            return False