from vec2 import Vec2
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
#some classes
class Boid:
	def __init__(self, position, velocity):
		self.position = position
		self.velocity = velocity
#######################################################################
#Some functions
def initBoids():
	drawBoids()
	moveBoids()

def moveBoids(boids):
	v1, v2, v3 = Vec2(0,0), Vec2(0,0), Vec2(0,0)
	for b in boids:
		v1 = checkRule1(b) 			#CHECK COHESION
		v2 = checkRule2(b)			#CHECK ALIGNMENT
		v3 = checkRule3(b)			#CHECK SEPARATION

		b.velocity = b.velocity + v1 + v2 + v3
		b.position = b.position + b.velocity

#COHESION: calculate the average position of the boid
def checkRule1(b):
	pc = Vec2(0,0)					#PERCIVED CENTER OF THE BOID FOR B
	for boid in boids:
		if (boid != b):
			pc = pc + boid.position
	pc = pc * (1/(len(boids) - 1))
	return (pc - b.position) * (1/100)


#ALIGNMENT: prevent the elements in the boid colide each others
#			take all the elements to close as possible
def checkRule2(b):
	c = Vec2(0,0) 			#CONTROL VECTOR FOR POSITION
	for boid in boids:
		if (boid != b and abs(boid.position - b.position) < 50):
			c = c - (boid.position - b.position)
	return c


#SEPARATION: calculate the parcived velocity of the flok 
def checkRule3(b):
	pv = Vec2(0,0)  		#PERCIVED VELOCITY OF THE BOID FOR B
	for boid in boids:
		if (boid != b):
			pv = pv + boid.velocity
	pv = pv * (1/ (len(boids) - 1))
	return (pv - b.velocity) * (1/100)


#######################################################################