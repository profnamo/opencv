# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 10:58:53 2025

@author: kalch
"""


import cv2 as cv
import sys
import numpy as np

img=cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE) 

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
bright_img = cv.add(img, 100)
    
cv.imshow('Gray original',img)    
cv.imshow('Gray Brightened', bright_img)

cv.waitKey()
cv.destroyAllWindows()