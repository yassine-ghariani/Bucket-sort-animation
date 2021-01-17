# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pygame
from NumberCase import NumberCase
import random


pygame.init()

dis_width = 1200
dis_height = 900
num = 20

dis = pygame.display.set_mode((dis_width, dis_height))
dis.fill((249,235,224))
pygame.display.set_caption('Sort Animation')
pygame.display.update()

font_style = pygame.font.SysFont('arial', 25)




l = [NumberCase(random.randint(0,10000), 55* i +75, 20, dis) for i in range(num)]


for x in l:
    x.display()
    
for i in range(10):
    msg = font_style.render('Bin ' + str(i), False, (96, 73, 44))
    dis.blit(msg, (10, 55 * i + 83))
    
    
def paquetter(l, n):
    dic = {i : [] for i in range(10)}
    for i in l:
        val = i.number
        binVal = (val // (10 ** n)) % 10
        i.move(i.x, 55 * binVal + 75)
        i.move(55* len(dic[binVal]) +75, i.y)
        
        dic[binVal].append(i)
    return dic

def depaquetter(dic):
    l=[]
    for i in range(10):
        for j in dic[i]:
            j.move(j.x, 75)
            j.move(55*len(l) + 75, j.y)
            j.move(j.x, 20)
            l.append(j)
    return l

n = 0
for i in l:
    if len(str(i.number)) > n:
        n = len(str(i.number))

for i in range(n):
    dic = paquetter(l, i)
    l = depaquetter(dic)

anim_over = False
while not anim_over:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            anim_over = True
pygame.quit()