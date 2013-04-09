import random
from square import *
import config

class Piece:
    def __init__(self, color):
        self.color = color
        self.squares = []
        self.location = config.START_LOCATION
        self.isFalling = True
    
    def getTop(self):
        points = [s.getRect().top for s in self.squares]
        return min(points)

    def getLeft(self):
        points = [s.getRect().left for s in self.squares]
        return min(points)

    def getBottom(self):
        points = [s.getRect().bottom for s in self.squares]
        return max(points)

    def getRight(self):
        points = [s.getRect().right for s in self.squares]
        return max(points)

    def getSquares(self):
        return self.squares

    def isActive(self):
        return self.isFalling

    def drop(self):
        new_bottom = self.getBottom() + config.SPEED
        (x,y) = self.location
        if new_bottom > config.SCREEN_Y - 1:
            self.isFalling = False
        else:
            self.location = (0,1)

    def left(self):
        new_left = self.getLeft() - config.SIDE_LENGTH
        (x,y) = self.location
        if new_left >= 0:
            self.location = (-1, 0)
        
    def right(self):
        new_right = self.getRight() + config.SIDE_LENGTH
        (x,y) = self.location
        if new_right <= config.SCREEN_X:
            self.location = (1,0)
        

    def move(self, pieces):
        #we already checked everything, except if there is a piece there
        if self.isActive():
            (x,y) = self.location
            x *= config.SIDE_LENGTH
            y *= config.SPEED
            
                        
            #apply movement
            collidedX = False
            collidedY = False
            for s in self.squares:
                r = s.getRect()
                r = r.move(x,0)
                if self.contains(pieces, r):
                    collidedX = True

            for s in self.squares:
                r = s.getRect()
                r = r.move(0,y)
                if self.contains(pieces, r):
                    collidedY = True

            #if we didn't hit anything with that move, move it.
            if not collidedX:
                for s in self.squares:
                    s.getRect().move_ip(x,0)
            # can we move down?
            if not collidedY:
                for s in self.squares:
                    s.getRect().move_ip(0,y)
            else:
                self.isFalling = False


    def getRectList(self):
        #this can change
        rectList = []
        for s in self.squares:
            rectList.append(s.getRect())
        return rectList

    #take a list of all other pieces to see if we collide
    def contains(self, pieces, newrect):
        collision_count = 0
        for piece in pieces:
            otherrects = piece.getRectList()
            collision_count = newrect.collidelist(otherrects)    
            if collision_count != -1:
                #there was a collision
                return True
        return False
            
        
    def repaint(self, surface):
        for s in self.squares:
            s.paint(surface)
    
        
    def rotate(self):
        raise NotImplementedError()
