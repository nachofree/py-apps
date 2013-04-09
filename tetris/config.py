TITLE = 'Tetris!'
NAME = 'Tetris!'

SCREEN_X = 240
SCREEN_Y = 320
COLUMNS = 10
SPACING = 0 #space between squares for each shape
            # not working, side length needs to figure this in

FRAMES_PER_SECOND = 30

BACKGROUND_COLOR = (0, 0, 0)
SIDE_LENGTH = SCREEN_X/COLUMNS

START_LOCATION = (0,0)
SPEED = 5

SHAPES = {0:"O",1:"L",2:"Z", 3:"I", 4:"T"} 
COLORS = ((255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255))
