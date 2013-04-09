import piece
from square import *

class TPiece(piece.Piece):
    def __init__(self, color):
        piece.Piece.__init__(self, color)

        (x, y) = self.location
        #this is still an o shape
        self.squares.append(Square((x,y), self.color))
        self.squares.append(Square((x+config.SIDE_LENGTH+config.SPACING,y), self.color))
        self.squares.append(Square((x,y+config.SIDE_LENGTH+config.SPACING), self.color))
        self.squares.append(Square((x+config.SIDE_LENGTH+config.SPACING,y+config.SIDE_LENGTH+config.SPACING), self.color))

