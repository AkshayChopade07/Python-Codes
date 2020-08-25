# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:30:01 2020

@author: Immortal
"""



import cv2 as cv 
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, img =camera.read()
    edges =cv.Canny(img,100,50)
    cv.imshow('Canny',edges)
    if cv.waitKey(5) == ord ('x'):
        break
    cv.destroyAllWindows()
    camera.release()
    
    
    
    
max(3,3.0,3.00)
