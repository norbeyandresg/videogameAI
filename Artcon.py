from Boids import *
import pygame
import sys

#define colors -----------
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

#constants ---------------
SCREEN_H = 800
SCREEN_W = 1200


#main class ----------------
class Control:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)

    def startScreen(self):
        global boids
        size = [SCREEN_W, SCREEN_H]
        screen = pygame.display.set_mode(size)

        man = Character(100, 10, 200, 200, screen)
        boids = createBoid(screen)
        running = True

        #screen event loop
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_w:
                        man.directions[0] = True
                    if e.key == pygame.K_s:
                        man.directions[1] = True
                    if e.key == pygame.K_a:
                        man.directions[2] = True
                    if e.key == pygame.K_d:
                        man.directions[3] = True
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_w:
                        man.directions[0] = False
                    if e.key == pygame.K_s:
                        man.directions[1] = False
                    if e.key == pygame.K_a:
                        man.directions[2] = False
                    if e.key == pygame.K_d:
                        man.directions[3] = False

            screen.fill(BLACK)
            man.draw(screen)
            man.move()
            checkDistance(boids, man)
            self.clock.tick(20)
            pygame.display.flip()

#super class ----------------
class Character:
    def __init__(self, life, dps, x, y, screen):
        self.life = life
        self.dps = dps
        self.x = x
        self.y = y
        self.speed = 10
        self.screen = screen
        pygame.draw.circle(self.screen, BLUE, (self.x, self.y), 10)
        self.directions = [False, False, False, False]

    def move(self):
        if self.directions[0]:
            self.y -= self.speed
        if self.directions[1]:
            self.y += self.speed
        if self.directions[2]:
            self.x -= self.speed
        if self.directions[3]:
            self.x += self.speed

    def reload():
        pass

    def getPos():
        return (self.x, self.y)

    def getLife():
        return self.life

    def draw(self, screen):
        pygame.draw.circle(self.screen, BLUE, (self.x, self.y), 10)

#enemy class ---------------
class Enemy(Character):
    pass


def checkDistance(boids, man):
    pc = Vec2(0,0)
    for b in boids:
        pc = pc + b.position
    pc = pc / len(boids)
    if (abs(Vec2(man.x, man.y) - pc)).mag() > 250 :
        drawBoids(boids, WHITE)
    else:
        drawBoids(boids, RED)

    if (abs(Vec2(man.x, man.y) - pc)).mag() > 200:
        moveBoids(boids, Vec2(man.x, man.y))


def main():
    pygame.init()
    pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Artcon")
    proc = Control()
    proc.startScreen()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
