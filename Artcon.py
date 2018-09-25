import pygame
import sys
import math

#import sprites -------------
char = pygame.image.load('M0.png')

#define colors -----------
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

#constants ---------------
SCREEN_H = 500
SCREEN_W = 800


#main class ----------------
class Control(object):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)

    def startScreen(self):
        size = [SCREEN_W, SCREEN_H]
        screen = pygame.display.set_mode(size)

        man = Character(200,200,char)
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
                elif e.type == pygame.MOUSEMOTION:
                    man.rotate()

            screen.fill(BLACK)
            man.draw(screen)
            man.move()
            man.rotate()
            self.clock.tick(20)
            pygame.display.flip()

#char class ----------------
class Character(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.speed = 10
        self.surface = img
        self.original_image = img
        self.rect = self.surface.get_rect()
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

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.surface = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.surface.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

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
