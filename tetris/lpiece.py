import piece
from square import *

class LPiece(piece.Piece):
    def __init__(self, color):
        piece.Piece.__init__(self, color)

        (x, y) = self.location
        self.squares.append(Square((x,y), self.color))
        self.squares.append(Square((x,y+config.SIDE_LENGTH+config.SPACING), self.color))
        self.squares.append(Square((x,y+2*config.SIDE_LENGTH+config.SPACING*2), self.color))
        self.squares.append(Square((x+config.SIDE_LENGTH+config.SPACING,y+2*config.SIDE_LENGTH+2*config.SPACING), self.color))

