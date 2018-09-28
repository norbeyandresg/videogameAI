import pygame
import sys
	
#define colors -----------
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

#constants ---------------
SCREEN_H = 500			#SCREE HEIGHT
SCREEN_W = 800			#SCREEN WIDTH
BOIDS_R = 5 			#BOID RADIUS

#######################################################################
#Some classes
class Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Boid(object):
	def __init__(self, position, velocity):
		self.position = position
		self.velocity = velocity
#######################################################################
#Some functions
def initBoids():
	drawBoids()
	moveBoids()

def moveBoids(boids):
	v1, v2, v3 = Vector(0,0), Vector(0,0), Vector(0,0)
	for B in boids:
		v1 = checkRule1(B) 			#CHECK COHESION
		v2 = checkRule2(B)			#CHECK 
		v3 = checkRule3(B)
#######################################################################