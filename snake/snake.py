#create a window
 #framerate
import pygame

class Snake:
    def __init__(self, width_in_pixels, height_in_pixels,
                 pixels_per_cell):
        self.width = width_in_pixels/pixels_per_cell
        self.height = height_in_pixels/pixels_per_cell
        self.pixels_per_cell = pixels_per_cell
        
        self.x_rate = 1
        self.y_rate = 0

        x = self.width/2
        y = self.height/2
        # create a snake
        # bunch of circles
        self.body = []
        for i in range(10):
            self.body.append( (x,y) )
            x-=1

    def up(self):
        self.x_rate = 0
        self.y_rate = -1
    def down(self):
        self.x_rate = 0
        self.y_rate = 1
    def right(self):
        self.x_rate = 1
        self.y_rate = 0
    def left(self):
        self.x_rate = -1
        self.y_rate = 0



    def move(self):
        #always moving
        # need to control the snake
        # move the snake
        self.body.pop()
        
        (x,y) = self.body[0]
        x+=self.x_rate
        y+=self.y_rate
        # figure out direction of movement and get next spot
        if x > self.width-1:
            x = 0
        if x < 0:
            x = self.width-1
        if y > self.height-1:
            y = 0
        if y < 0:
            y = self.height-1
        #if we intersect with ourself, death        
        self.body.insert(0, (x,y))

    def paint(self, surface):
        color = (200, 127, 127)
        for (x,y) in self.body:
            xpixel = x * self.pixels_per_cell + self.pixels_per_cell/2
            ypixel = y * self.pixels_per_cell + self.pixels_per_cell/2
            rpixel = self.pixels_per_cell / 2
            pygame.draw.circle(surface, color, (xpixel, ypixel), rpixel)

    

