# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:32:51 2021

@author: Yassine
"""

import pygame

class NumberCase:
    def __init__(self, number, x, y, dis):
        self.number = number
        self.x = x
        self.y = y
        self.dis = dis
        self.width = 50
        self.color = (32,138,174)
        self.font_style = pygame.font.SysFont('arial', 25)
        self.s = pygame.Surface((self.width, self.width))
        self.s.fill(self.color)
        
    
    def display(self):
        self.s.fill(self.color)
        
        msg = self.font_style.render(str(self.number), False, (96, 73, 44))
        self.s.blit(msg, (2 , 10))
        
        self.dis.blit(self.s,(self.x, self.y))
        
        
        
        pygame.display.update()
    def move(self, target_x, target_y):
        if target_x - self.x != 0:
            move_x = (target_x - self.x)/ abs(target_x - self.x)
        else:
            move_x = 0
        if target_y - self.y != 0:
            move_y = (target_y - self.y)/ abs(target_y - self.y)
        else:
            move_y = 0
        
        move = 0
        
        while self.y != target_y or self.x != target_x:
            if move % 4 ==0 :
                self.color = (249,235,224)
                self.display()
                
                self.y += move_y
                self.x += move_x
                
                self.color = (32,138,174)
                self.display()
            move += 1

        self.color = (13, 33, 73)
        self.display()
            