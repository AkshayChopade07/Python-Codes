# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:54:39 2020

@author: Immortal
"""


import turtle
color=['Red','Purple','Green','Blue','White','Orange']
turtle.bgcolor('Black')
for x in range(360):
    turtle.pencolor(color[x%6])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)
    
