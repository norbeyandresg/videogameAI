from vec2 import Vec2
import pygame
import sys
import random

#define colors -----------
RED = (255,0,0)
GREEN = (0,255,0)
#constants ---------------
SCREEN_H = 500
SCREEN_W = 800
BOIDS_R = 8 			#BOID RADIUS
SPEED_LIMIT = 10 		#SPEED LIMIT FOR THE BOIDS

#######################################################################
#BOID OBJECT CLASS
class Boid:
	def __init__(self, position, velocity, screen):
		self.position = position
		self.velocity = velocity
		self.screen = screen
		pygame.draw.circle(screen, GREEN, (int(self.position.x), int(self.position.y)), BOIDS_R)
#######################################################################
#BOIDS MANIPULATION FUNCTIONS
def initBoids():
	drawBoids()
	moveBoids()

def drawBoids(boids):
	for b in boids:
		pygame.draw.circle(b.screen, GREEN, (int(b.position.x), int(b.position.y)), BOIDS_R)

def moveBoids(boids, target):
	v1, v2, v3 = Vec2(0,0), Vec2(0,0), Vec2(0,0)
	for b in boids:
		v1 = checkRule1(boids, b) 			#CHECK COHESION
		v2 = checkRule2(boids, b, target)	#CHECK ALIGNMENT
		v3 = checkRule3(boids, b)			#CHECK SEPARATION
		trg = getTarget(b, target)

		b.velocity = b.velocity + v1 + v2 + v3 + trg
		limit_speed(b)
		b.position = b.position + b.velocity + boundPos(b)


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
def checkRule2(boids, b, target):
	c = Vec2(0,0) 			#CONTROL VECTOR FOR POSITION
	targetPos = Vec2(target.x, target.y)
	for boid in boids:
		if (boid != b and abs(boid.position - b.position) < 20):
			c = c - (boid.position - b.position)
	if (abs(targetPos - b.position ) < 20):
		c = c - (targetPos / b.position)
	if (c.mag() > 0):
		c = c.norm()
	return c


#SEPARATION: calculate the percived velocity of the flok
def checkRule3(boids, b):
	pv = Vec2(0,0)  		#PERCIVED VELOCITY OF THE BOID FOR B
	for boid in boids:
		if (boid != b):
			pv = pv + boid.velocity
	pv = pv * (1/ (len(boids) - 1))
	pv = pv - b.velocity
	if (pv.mag() > 0):
		pv = pv.norm()
	return pv

def createBoid(screen):
	boids = []

	for i in range (10):
		position = Vec2(random.randrange(SCREEN_W), random.randrange(SCREEN_H))
		velocity = Vec2(0,0)
		p = Boid(position, velocity, screen)
		boids.append(p)
	return boids

def getTarget(b, target):
	target = target - b.position
	if (target.mag() > 0):
		target = target.norm()
	return target

def limit_speed(b):
	v = Vec2(0,0)

	if (abs(b.velocity) > SPEED_LIMIT):
		b.velocity = (b.velocity / abs(b.velocity)) * SPEED_LIMIT

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
