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

    X = 0
    Y = 1

    def __init__(self, imagefile, speed=[0, 0], direction=[0, 0]):
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
        ''' Set speed in x and y direction 
        
        Speed is given as a list with two elements 
        where speed[0] is number of pixels to move in x-direction
        and speed[1] is number of pixels to move in y-direction
        for each move().

        Se also set_direction().
        '''
        self._speed = speed

    def get_speed(self):
        return self._speed

    def get_speed_x(self):
        return self._speed[self.X]

    def get_speed_y(self):
        return self._speed[self.Y]

    def set_direction(self, direction):
        ''' Set direction in x and y direction 
        
        Direction is given as a list with two elements 
        where direction[0] indicates left (-1) or right (+1)
        and direction[1] indicates up (-1) or down (+1).

        Se also set_speed().
        '''
        self._direction = direction

    def get_speed(self):
        return self._speed

    def get_odometer(self):
        return self._odometer

    def move(self):
        self._odometer += math.sqrt(self._speed[0]**2 + self._speed[1]**2) # Pythagoras
        self.rect = self.rect.move([self._speed[self.X]*self._direction[self.X], 
                                    self._speed[self.Y]*self._direction[self.Y]])

    def flip_horiz(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self._direction[0] *= -1

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
