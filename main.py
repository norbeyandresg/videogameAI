# Artcon Game
import os, sys
import pygame as pg
from vec2 import Vec2
import userControl, entity, img_collect

# Initialize pygame
pg.init()
#pg.mixer.init()


# Assets dicetories
main_folder = os.path.dirname(__file__)
image_folder = os.path.join( main_folder, 'img' )
sound_folder = os.path.join( main_folder, 'snd' )
music_folder = os.path.join( main_folder, 'mus' )

# Fonts
font = pg.font.SysFont( 'couriernew', 24 )

# Settings >> gametitle, window settings, etc
GAME_TITLE = 'Artcon'
GAME_ICON = pg.image.load( os.path.join( image_folder, 'icon.png') )

WIDTH = 640
HEIGHT = 480
FPS = 90

SCORE = 0

pg.display.set_caption( GAME_TITLE )
pg.display.set_icon( GAME_ICON )
GAME_SURFACE = pg.display.set_mode( ( WIDTH, HEIGHT ))
clock = pg.time.Clock()

# Color constants
class Palette:
    def __init__( self ):
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

def leave():
    pg.quit()
    sys.exit()

def detect ( obj ):
    global SCORE
    for i in range( len ( player.laser ) ):

        if ( obj.collide( player.laser[i] ) == True ):
            player.laser[i].reset()
            obj.reset()
            SCORE += 10

def draw_text( x, y, text ):
    WHITE = ( 255, 255, 255 )
    txt = font.render( str( text ), True, WHITE )
    GAME_SURFACE.blit( txt, ( x, y) )

# Building objects
user = userControl.Controller()
player = entity.Player()
enemy = entity.Enemy()

bad_guy = [
    entity.Enemy(),
    entity.Enemy(),
    entity.Enemy(),
    entity.Enemy(),
    entity.Enemy(),
    entity.Enemy(),
    entity.Enemy()
]

w = bad_guy[0].rect.width

for i in range( len( bad_guy ) ):
    bad_guy[i].spawn( ( WIDTH + w, 100 + ( i * 50 ) ) )


# Collective list
all_sprites = img_collect.Collection()
enemy_sprites = img_collect.EnemyCollection()
all_sprites.add( player )
all_sprites.combine( player.laser )
enemy_sprites.combine( bad_guy )


# Register inputs
col = Palette()
running = True

while running:

    # Run at this rate
    clock.tick( FPS )
    contents =  user.run()

    # Process input
    player.run( contents )
    all_sprites.run()
    enemy_sprites.run( bad_guy, player )

    # Looking for the Laser
    for i in range( len( bad_guy ) ):
        detect( bad_guy[i] )

    # Drawing
    GAME_SURFACE.fill( col.BLACK )
    all_sprites.draw( GAME_SURFACE )
    enemy_sprites.draw( GAME_SURFACE )

    # Draw the hud
    draw_text( 10, 10, 'Score >> '+ ' ' + str( SCORE ) )

    # Update the screen
    pg.display.update()

leave()
