import pygame

SHIPSPEED = 3

def loadImage(filename):
    datadir = "./data/"
    image = pygame.image.load(datadir+filename)
    image = image.convert()
    return image, image.get_rect()


#space class
class Space:
    def __init__(self):
        self.image, self.rect = loadImage("stars.bmp")
        
    def paint(self, screen):
        screen.blit(self.image, self.rect)
#ship class
class Ship(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, shiptype='frenemy'):
        pygame.sprite.Sprite.__init__(self)

        self.x = start_x
        self.y = start_y
        self.dx = 0.0
        self.dy = 0.0
        self.shiptype = shiptype
        self.bullets = []
        self.moving = False
        self.alive = True

        if shiptype == 'enemy':
            self.image, self.rect = loadImage("eship.bmp")
        else:
            self.image, self.rect = loadImage("ship.bmp")

        self.rect.bottomleft = (self.x, self.y)

    def isAlive(self):
        return self.alive

    def right(self):
        if self.moving:
            self.dx = 0.0
            self.moving = False
        else:
            self.dx = SHIPSPEED
            self.moving = True
        
    def left(self):
        if self.moving:
            self.dx = 0.0
            self.moving = False
        else:
            self.dx = -SHIPSPEED
            self.moving = True

    def getRect(self):
        return self.rect
    
    def die(self):
        self.alive = False
            
    def checkHits(self, enemyShips):

        
        for ship in enemyShips:
            for b in self.bullets:
                if ship.getRect().contains(b.getRect()):
                    ship.die()
                    b.die()

    def fire(self):
        self.bullets.append(Bullet(self.rect.center))


    def paint(self, screen):
        if len(self.bullets)>0:
            for bullet in self.bullets:
                bullet.paint(screen)

            for bullet in self.bullets:
                if bullet.getStatus() == False:
                    self.bullets.remove(bullet)

        newrect = self.rect.move((self.dx, self.dy))
        area = screen.get_rect()

        if area.contains(newrect):
            if not self.rect.right > area.right or not self.rect.left < area.left:
                self.rect = newrect

        screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadImage("fire.bmp")
        self.rect.bottomleft = (x, y)
        
        self.x = x
        self.y = y
        self.active = True

    def getRect(self):
        return self.rect

    def paint(self, screen):
        newrect = self.rect.move((0, -1))
        area = screen.get_rect()

        if area.contains(newrect):
            self.rect = newrect
            screen.blit(self.image, self.rect)
        else:
            self.active = False

    def die(self):
        self.active = False

    def getStatus(self):
        return self.active
        
