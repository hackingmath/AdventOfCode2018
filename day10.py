import pygame
import time
from random import randint, uniform
from math import pi, sqrt, cos, sin, atan2

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

lines = list()
for line in open('day10.txt'):
    lines.append(line)#.split())
print(len(lines),lines)
locs = list()
for i,l in enumerate(lines):
    # try:
    #print("i,l:",i,l)
    x,y = int(l[10:16]), int(l[18:24])
    xvel, yvel = int(l[36:38]), int(l[40:42])
    print("x,y:",x,y)
    locs.append([x,y,xvel,yvel])
    # except:
    #     print("breaks at i:",i)


print(len(locs),locs[:5])

def part1(testing=False):
    pass

def part2(testing=False):
    pass



# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

width,height = 600,600

# set up display
pygame.init()
screen = pygame.display.set_mode([width, height])

class Dot(object):
    def __init__(self,x,y,xvel,yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.x += self.xvel
        self.y += self.yvel
        

#in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)

pygame.display.set_caption('Pygame Window') #add your own caption!
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0 #frame count

# loop until user clicks the close button
done = False

#Rendering the Game
xpos,ypos = 300,300

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if pygame window is closed by user
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xpos -= 20
    if keys[pygame.K_RIGHT]:
        xpos += 20

    if keys[pygame.K_p]:
        if FPS == 60:
            FPS = 300  #faster display
        else:
            FPS = 60
    # fill the screen with background color
    screen.fill(BLACK)

    #pygame.draw.polygon(screen, WHITE, [(100, 200), (xpos,ypos), (524, 307), (500, 200)], 0)
    pygame.draw.rect(screen, WHITE, [xpos,ypos, 150,200])
    pygame.draw.line(screen, GREEN, [100,100],[200,300],3)
    pygame.draw.circle(screen,RED,[400,100],50)

    counter += 1

    pygame.display.update()

    # for saving screenshots:
    # if counter %5 == 0:
    # capture(screen, 'Capture{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)


print("Time (s.):",time.time()-start)
pygame.quit()
