''' Pygame Car Model

TODO: implement movement in y direction

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''

import math
import pygame

class Car(pygame.sprite.Sprite):
    '''A simple car model'''
    def __init__(self, imagefile, speed=0, direction=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self._speed = speed
        self._direction = direction
        self._odometer = 0

    def set_xpos(self, pos):
        self.rect.left = pos 

    def get_xpos(self):
        return self.rect.left

    def set_ypos(self, pos):
        self.rect.top = pos 

    def get_ypos(self):
        return self.rect.top

    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    def get_odometer(self):
        return self._odometer

    def set_direction(self, direction):
        '''Set the car direction

        The direction is given as a list:
        [1, 0] : moving to the right (0 deg)
        [-1, 0] : moving to the left (180 deg)
        [0, -1] : moving up (90 deg)
        [0, 1] : moving down (270 deg)
        '''
        self._direction = direction

    def move(self):
        move_x = self._direction[0]*self._speed
        move_y = self._direction[1]
        self._odometer += math.sqrt(move_x**2 + move_y**2) # Pythagoras
        self.rect = self.rect.move([move_x, move_y])

    def turn(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self._direction[0] *= -1

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
