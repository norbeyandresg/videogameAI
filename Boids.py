from vec2 import Vec2
import pygame
import sys
import random 
	
#define colors -----------
RED = (255,0,0)

#constants ---------------
SCREEN_H = 500
SCREEN_W = 800
BOIDS_R = 10 			#BOID RADIUS

#######################################################################
#BOID OBJECT CLASS
class Boid:
	def __init__(self, position, velocity, screen):
		self.position = position
		self.velocity = velocity
		self.screen = screen
		pygame.draw.circle(screen, RED, (int(self.position.x), int(self.position.y)), BOIDS_R)
#######################################################################
#BOIDS MANIPULATION FUNCTIONS
def initBoids():
	drawBoids()
	moveBoids()

def drawBoids(boids):
	for b in boids:
		pygame.draw.circle(b.screen, RED, (int(b.position.x), int(b.position.y)), BOIDS_R)

def moveBoids(boids):
	v1, v2, v3 = Vec2(0,0), Vec2(0,0), Vec2(0,0)
	for b in boids:
		v1 = checkRule1(boids, b) 			#CHECK COHESION
		v2 = checkRule2(boids, b)			#CHECK ALIGNMENT
		v3 = checkRule3(boids, b)			#CHECK SEPARATION

		b.velocity = b.velocity + v1 + v2 + v3
		b.position = b.position + b.velocity

#COHESION: calculate the average position of the boid
def checkRule1(boids, b):
	pc = Vec2(0,0)					#PERCIVED CENTER OF THE BOID FOR B
	for boid in boids:
		if (boid != b):
			pc = pc + boid.position
	pc = pc * (1/(len(boids) - 1))
	return (pc - b.position) * (1/100)


#ALIGNMENT: prevent the elements in the boid colide each others
#			take all the elements to close as possible
def checkRule2(boids, b):
	c = Vec2(0,0) 			#CONTROL VECTOR FOR POSITION
	for boid in boids:
		if (boid != b and abs(boid.position - b.position) < 5):
			c = c - (boid.position - b.position)
	return c


#SEPARATION: calculate the parcived velocity of the flok 
def checkRule3(boids, b):
	pv = Vec2(0,0)  		#PERCIVED VELOCITY OF THE BOID FOR B
	for boid in boids:
		if (boid != b):
			pv = pv + boid.velocity
	pv = pv * (1/ (len(boids) - 1))
	return (pv - b.velocity) * (1/100)

def createBoid(screen):
	boids = []

	for i in range (10):
		position = Vec2(random.randrange(SCREEN_W), random.randrange(SCREEN_H))
		velocity = Vec2(0,0)
		p = Boid(position, velocity, screen)
		boids.append(p)
	return boids
#######################################################################


