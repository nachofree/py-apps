import config
import pygame
import game

from opiece import *
from ipiece import *
from zpiece import *
from lpiece import *
from tpiece import *

import random


class Tetris(game.Game):
    def __init__(self, name, 
                 width, height,
                 frames_per_second):
        game.Game.__init__(self, name,
                           width,
                           height)

        #hold resting piecesf
        self.pieces = []
        #start first piece
        self.current_p = self.generatePiece()


    def generatePiece(self):
        color = random.choice(config.COLORS)
        pieceType = random.choice(config.SHAPES.values())
        fn = pieceType + "Piece( "+str(color)+" )"
        p = eval(fn)
        return p
        

    def game_logic(self, keys, newkeys):
        if self.current_p.isActive():
            #apply the drop
            self.current_p.drop()
            #check for keys
            if pygame.K_LEFT in newkeys:
                self.current_p.left()
            if pygame.K_RIGHT in newkeys:
                self.current_p.right()
            if pygame.K_UP in newkeys:
                self.current_p.rotate()
            

            self.current_p.move(self.pieces)
        else:
            #not active
            self.pieces.append(self.current_p)
            self.current_p = self.generatePiece()



    def paint(self, surface):
        # redraw the screen
        surface.fill(config.BACKGROUND_COLOR)
        #paint current piece
        self.current_p.repaint(surface)
        #paint the other ones
        for p in self.pieces:
            p.repaint(surface)
        
