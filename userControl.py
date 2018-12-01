# A .py with user controls
# Class { Controller, Player, }
import pygame as pg
import os, sys

pg.init()

class Controller:
    def __init__( self ):
        self.key_right = 0
        self.key_left = 0
        self.key_up = 0
        self.key_down = 0

        self.key_shoot = 0
        self.key_pause = 0

        self.keys_pressed = [
            self.key_right,
            self.key_left,
            self.key_up,
            self.key_down,

            self.key_pause,
            self.key_shoot,
        ]

    def run( self ):
        for evn in pg.event.get():
            if evn.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif evn.type == pg.KEYDOWN:
                # For pressing key
                if evn.key == pg.K_a:
                    self.key_left = -1
                elif evn.key == pg.K_w:
                    self.key_up = -1
                elif evn.key == pg.K_d:
                    self.key_right = 1
                elif evn.key == pg.K_s:
                    self.key_down = 1
                elif evn.key == pg.K_RETURN:
                    self.key_pause = 1
                elif evn.key == pg.K_j:
                    self.key_shoot = 1
                else:
                    pass


            elif evn.type == pg.KEYUP:
                # For releasing key
                if evn.key == pg.K_a:
                    self.key_left = 0
                elif evn.key == pg.K_w:
                    self.key_up = 0
                elif evn.key == pg.K_d:
                    self.key_right = 0
                elif evn.key == pg.K_s:
                    self.key_down = 0
                elif evn.key == pg.K_RETURN:
                    self.key_pause = 0
                elif evn.key == pg.K_j:
                    self.key_shoot = 0
                else:
                    pass



        # Modify  the list
        self.keys_pressed[0] = self.key_right
        self.keys_pressed[1] = self.key_left
        self.keys_pressed[2] = self.key_up
        self.keys_pressed[3] = self.key_down

        self.keys_pressed[4] = self.key_pause
        self.keys_pressed[5] = self.key_shoot


        # Return the list >>
        return self.keys_pressed
