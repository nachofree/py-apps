import math
import pygame

from point import Point
import config


class Square:
    def __init__(self, top_left_position, color):
        (x, y) = top_left_position
        self.position = Point(x, y)
        self.color = color
        self.active = True        
        self.rect = pygame.Rect(x, y, config.SIDE_LENGTH, config.SIDE_LENGTH) 

    def move(self):
        x = self.position.x + self.pull.x
        y = self.position.y + self.pull.y
        if x >= config.SCREEN_X:
            x -= config.SCREEN_X
        if x < 0.0:
            x += config.SCREEN_X
        if y >= config.SCREEN_Y:
            y -= config.SCREEN_Y
        if y < 0.0:
            y += config.SCREEN_Y
        self.position = Point(x, y)
    
    def getRect(self):
        return self.rect

    def setRect(self, r):
        self.rect = r

    def paint(self, surface):
        if not self.active:
            return
        pygame.draw.rect(surface, self.color, self.rect)
    
