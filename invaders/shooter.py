#shooter.py

import pygame
import game
import space

class Shooter(game.Game):
    def __init__(self, name, width, height, frames_per_second):
        game.Game.__init__(self, name, width, height, frames_per_second)
        self.bg = space.Space()
        self.ship = space.Ship(10, height-10)
        self.enemies = []
        offset_x = 10
        offset_y = 40
        spacing = 50
        for row in range(4):
            for col in range(3):
                self.enemies.append(space.Ship(spacing * row + offset_x, spacing * col+offset_y, 'enemy'))

    def game_logic(self, keys, newkeys):
        if pygame.K_LEFT in newkeys:
            self.ship.left()

        elif pygame.K_RIGHT in newkeys:
            self.ship.right()

        if pygame.K_UP in newkeys:
            self.ship.fire()
        
        self.ship.checkHits(self.enemies)
        
        for enemy in self.enemies:
            if not enemy.isAlive():
                self.enemies.remove(enemy)
        
    def paint(self, surface):
        self.bg.paint(surface)
        self.ship.paint(surface)
        for enemy in self.enemies:
            enemy.paint(surface)
        
