import userControl, sys, random
import pygame as pg
from vec2 import Vec2

pg.init()

WIDTH = 640
HEIGHT = 480

REST = (-WIDTH, -HEIGHT)

class Entity:
    def run( self ):
        pass

    def draw( self, surface ):
        surface.blit( self.SURF, [ self.rect.topleft, self.rect.topleft] )

    def collide( self, other ):
        # Initialize variables
        x = y = 0

        # Check horizontal colitions
        if ( ( self.rect.x + x < other.rect.x ) and ( ( self.rect.x + x ) + self.rect.width > other.rect.x ) ) \
        or ( ( self.rect.x + x < other.rect.x + other.rect.width ) and ( ( self.rect.x + x ) + self.rect.width > other.rect.x + other.rect.width ) ):

            # Check vertical colitions
            if ( ( self.rect.y + x < other.rect.y ) and ( ( self.rect.y + y ) + self.rect.height > other.rect.y ) ) \
            or ( ( self.rect.y + y < other.rect.y + other.rect.height ) and ( ( self.rect.y + y ) + self.rect.height > other.rect.y + other.rect.height ) ):

                return True

        return False


class Laser( Entity ):
    def __init__( self ):
        # Active variables
        self.active = False
        self.DEPENDENCE = True

        # Masking variables
        self.SURF = pg.Surface( ( 24, 8 ))
        self.SURF.fill( ( 0, 255, 0 ))

        self.rect = self.SURF.get_rect()
        self.rect.x, self.rect.y = REST

        self.mspd = 14

    def reset( self ):
        self.active = False
        self.rect.x, self.rect.y = REST

    def bounds( self ):
        if ( self.rect.left > WIDTH ):
            Laser.reset( self )

    def run( self ):
        if ( self.active) :
            self.rect.x += self.mspd
            Laser.bounds( self )

    def blast( self, XnY ):
        if ( self.active == False ):
            self.active = True
            self.rect.centerx, self.rect.centery = XnY



class Player( Entity ):
    def __init__( self ):
        # Build instance
        self.laser = [ Laser(), Laser(), Laser() ]
        self.DEPENDENCE = False
        self.healt = 3
        self.score = 0

        self.pressed = False

        # Masking variables
        self.SURF = pg.Surface( ( 32, 32 ))
        self.SURF.fill( ( 0, 0, 255 ))

        self.rect = self.SURF.get_rect()

        self.rect.centerx = WIDTH // 4
        self.rect.centery = HEIGHT // 2
        self.hspd = 0
        self.vspd = 0
        self.mspd = 4

        self.px = self.py = 0

    def run( self, key_list ):
        # Unpackage the list
        keyR, keyL, keyU, keyD, keyP, keyS = key_list

        # Process informatino from the key_list
        moveH = keyR + keyL
        moveV = keyU + keyD

        # SHOOTING
        if ( keyS ):
            for i in range( len( self.laser ) ):
                if ( self.laser[ i ].active == False ):

                    if ( self.pressed == False ):
                        self.pressed = True
                        self.laser[i].blast( ( self.rect.centerx + 16, self.rect.centery ) )
        else:
            self.pressed = False

        self.hspd = moveH * self.mspd
        self.vspd = moveV * self.mspd

        self.rect.centerx += self.hspd
        self.rect.centery += self.vspd

        # Bounds checking
        if ( self.rect.right > WIDTH ):
            self.rect.right = WIDTH
        if ( self.rect.left < 0 ):
            self.rect.left = 0
        if ( self.rect.bottom > HEIGHT ):
            self.rect.bottom = HEIGHT
        if ( self.rect.top < 0 ):
            self.rect.top = 0

    def draw( self, surface ):
        surface.blit( self.SURF, [ self.rect.topleft, self.rect.topleft] )


# Enemi classes
class Enemy( Entity ):
    def __init__( self ):
        self.DEPENDENCE = True
        self.mspd = 5

        self.active = False
        self.SURF = pg.Surface( ( 32, 32 ) )
        self.SURF.fill( ( 200, 100, 0 ) )

        self.rect = self.SURF.get_rect()
        self.rect.x, self.rect.y = REST

    def spawn( self, XnY ):
        if ( self.active == False ):
            self.rect.x, self.rect.y = XnY
            self.active = True


    def reset( self ):
        self.rect.left = WIDTH
        self.rect.bottom = random.randint( self.rect.height, HEIGHT )
        self.active = True


    def run( self, boids, target ):
        v1, v2, v3 = Vec2(0,0), Vec2(0,0), Vec2(0,0)
        if ( self.active == True ):
            v1 = checkRule1(boids, b) 			#CHECK COHESION
    		v2 = checkRule2(boids, b, target)	#CHECK ALIGNMENT
    		v3 = checkRule3(boids, b)			#CHECK SEPARATION
    		trg = getTarget(b, target)

            vel = Vec2(self.mspd, self.mspd) + v1 + v2 + v3 + trg
            self.mspd = vel.x
            limit_speed(self)
            self.rect.x -= self.mspd
            self.rect.y -= self.mspd

    def draw( self, surface ):
        surface.blit( self.SURF, [ self.rect.topleft, self.rect.topleft ] )



#COHESION: calculate the average position of the boid
def checkRule1(boids, b):
	pc = Vec2(0,0)					#PERCIVED CENTER OF THE BOID FOR B
	for boid in boids:
		if (boid != b):
			pc = pc + Vec2(boid.rect.x , boid.rect.y)
	pc = pc * (1/(len(boids) - 1))
	return (pc - Vec2(b.rect.x, b.rect.y)) * (1/100)


#ALIGNMENT: prevent the elements in the boid colide each others
#			take all the elements to close as possible
def checkRule2(boids, b, target):
	c = Vec2(0,0) 			#CONTROL VECTOR FOR POSITION
	targetPos = Vec2(target.rect.x, target.rect.y)
	for boid in boids:
		if (boid != b and abs(Vec2(boid.rect.x, boid.rect.y) - Vec2(b.rect.x, b.rect.y)) < 20):
			c = c - (Vec2(boid.rect.x, boid.rect.y) - Vec2(b.rect.x, b.rect.y))
	if (abs(targetPos - Vec2(b.rect.x, b.rect.y) ) < 20):
		c = c - (targetPos / Vec2(b.rect.x, b.rect.y))
	if (c.mag() > 0):
		c = c.norm()
	return c


#SEPARATION: calculate the percived velocity of the flok
def checkRule3(boids, b):
	pv = Vec2(0,0)  		#PERCIVED VELOCITY OF THE BOID FOR B
	for boid in boids:
		if (boid != b):
			pv = pv + Vec2(boid.mspd, boid.mspd)
	pv = pv * (1/ (len(boids) - 1))
	pv = pv - Vec2(b.mspd, b.mspd)
	if (pv.mag() > 0):
		pv = pv.norm()
	return pv

def getTarget(b, target):
	target = target - Vec2(b.rect.x, b.rect.y)
	if (target.mag() > 0):
		target = target.norm()
	return target

def limit_speed(b):
	v = Vec2(0,0)

	if (abs(Vec2(b.mspd, b.mspd)) > SPEED_LIMIT):
        temp = (Vec2(b.mspd, b.mspd) / abs(Vec2(b.mspd, b.mspd))) * SPEED_LIMIT
		b.mspd = temp.x

def boundPos(b):
	xmin, ymin = 0,0
	xmax, ymax = SCREEN_W, SCREEN_H
	v = Vec2(0,0)

	if (b.position.x < xmin):
		v.x = 10
	elif (b.position.x > xmax):
    	v.x = -10

	if (b.position.y < ymin):
		v.y = 10
	elif (b.position.y > ymax):
		v.y = -10

	return v
#######################################################################
