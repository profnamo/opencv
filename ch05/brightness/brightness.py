# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 10:58:53 2025

@author: kalch
"""


import cv2 as cv
import sys
import numpy as np

img=cv.imread('lenna.bmp') 

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
bright_img = cv.add(img, np.array([100.0]))
    
cv.imshow('lenna',img)    
cv.imshow('Brightened', bright_img)

cv.waitKey()
cv.destroyAllWindows()