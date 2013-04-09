import game
from snake import *

class SnakeGame(game.Game):
    def __init__(self):
        game.Game.__init__(self, "Snake", 640, 480, 10)
        #create an instance of snake
        self.snake = Snake(640, 480, 20)

    def paint(self, surface):
        surface.fill((0,0,0))
        self.snake.paint(surface)
    
    def game_logic(self, keys, newkeys):
        if pygame.K_UP in newkeys:
            self.snake.up()
        if pygame.K_DOWN in newkeys:
            self.snake.down()
        if pygame.K_LEFT in newkeys:
            self.snake.left()
        if pygame.K_RIGHT in newkeys:
            self.snake.right()



        self.snake.move()
    
def main():
    s = SnakeGame()
    s.main_loop()

main()
