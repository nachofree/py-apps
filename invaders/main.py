#!/usr/bin/python

import sys
#import config
import shooter

def main():

    myshooter = shooter.Shooter("Space Invaders", 640, 480, 60)

    myshooter.main_loop()
    
main()
