# -*- coding: utf-8 -*-

#ADDING GAUSSIAN NOISE

import cv2 as cv
import numpy as np

im = cv.imread('./pics/img5.tif', 0)
im = im/255

#create gaussian noise

x, y = im.shape
mean = 0
var = 0.01
sigma = np.sqrt(var)
n= np.random.normal(loc = mean,
                    scale = sigma,
                    size = (x, y))

#add gaussian noise

g = im + n

res = np.hstack((im, g)) #stacking images side-by-side
cv.imwrite('res.png',res)