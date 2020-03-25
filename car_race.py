''' Pygame Car Race Animation

Simple program to demonstrate animation in pygame, 
and to give my students a starting point for making new animations.

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''

import sys
import random
import pygame
import car_model as car

pygame.init()
#pygame.font.init()

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 768

FPS = 25
MAX_CARS = 14
MAX_CAR_MODELS = 8
MAX_SPEED = 10

WHITE = pygame.Color(255, 255, 255)
LIGHTGRAY = pygame.Color(211, 211, 211)
SILVER = pygame.Color(192, 192, 192)
DARKGRAY = pygame.Color(169, 169, 169)
GRAY = pygame.Color(128, 128, 128)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Car Race')
myfont = pygame.font.SysFont(pygame.font.get_default_font(), 72)

cars = [None]*MAX_CARS # list for storage of car objects
lanes = [None]*MAX_CARS # list of lane numbers


for i in range(0, MAX_CARS): # generating car objects
    car_img = 'img/car_' + str(random.randint(1, MAX_CAR_MODELS)) + '.png'
    car_speed = random.randint(1, MAX_SPEED)
    cars[i] = car.Car(car_img, [1, 0], [-1, 0])
    cars[i].set_ypos(50 + i * 50)
    cars[i].set_xpos(DISPLAY_WIDTH)
    lanes[i] = myfont.render(str(i+1), False, LIGHTGRAY)

racing = True
leading_car = -1
last_car = -1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    last_car_dist = DISPLAY_WIDTH*2
    leading_car_dist = 0
    
    screen.fill(SILVER) # re-painting the screen

    if racing:
        for i in range(0, MAX_CARS):
            # move cars and paint them on the screen
            screen.blit(lanes[i],(DISPLAY_WIDTH-100, (i+1)*50))
            cars[i].move()
            screen.blit(cars[i].image, cars[i].rect)

            # new speed is the mean of prior speed and a random number
            x_speed = (random.randint(0, MAX_SPEED)+cars[i].get_speed_x()) // 2
            cars[i].set_speed([x_speed, 0])

            if cars[i].get_xpos() < 0:
                # car has reached left edge of screen, turning it
                cars[i].flip_horiz()
                cars[i].set_xpos(1) # move the car 1px away from edge

            if cars[i].get_odometer() < last_car_dist:
                # keeping track of the last car in the field
                last_car_dist = cars[i].get_odometer()
                last_car = i
            elif cars[i].get_odometer() > leading_car_dist:
                # keeping track of the first car in the field
                leading_car_dist = cars[i].get_odometer()
                leading_car = i
            else:
                pass

        #print('Leading #{}  dist: {} - Last #{}  dist: {}'.format(leading_car, leading_car_dist, last_car, last_car_dist))

        if cars[leading_car].get_xpos() >= DISPLAY_WIDTH: 
            # last car has finished the race
            racing = False
            text = 'The race is over, car #{} won'.format(leading_car+1)
        else:
            text = 'Car #{} is in the lead'.format(leading_car+1)
    
    textsurface = myfont.render(text, False, GRAY)
    screen.blit(textsurface,(0, 0))
    pygame.display.flip()
    clock.tick(FPS)
