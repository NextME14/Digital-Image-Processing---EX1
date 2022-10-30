# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:53:14 2022

@author: nethm
"""

#Draw histogram of an image, try histogram equalization.

import cv2 as cv
import numpy as np

im = cv.imread('./pics/img6.tif', 0)
hist = cv.calcHist([im],[0],None,[256],[0,256])

#min intensity is 10, max intensity is 81

equ = cv.equalizeHist(im)

hist2 = cv.calcHist([equ],[0],None,[256],[0,256])

import matplotlib.pyplot as plt
plt.figure()
plt.plot(hist, 'r-') #red curve-original
plt.plot(hist2, 'b-') #blue curve- equalized

res = np.hstack((im,equ)) #stacking images side-by-side
cv.imwrite('res.png',res)