#!/usr/bin/python
import sys
import config
import tetris

def main():

    t = tetris.Tetris(config.NAME,
                       config.SCREEN_X, config.SCREEN_Y,
                       config.FRAMES_PER_SECOND)
    t.main_loop()
    
main()
