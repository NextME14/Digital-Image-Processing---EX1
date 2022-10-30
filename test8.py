# -*- coding: utf-8 -*-

#INTENSITY NORMALIZATION

import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt

img = cv.imread('./pics/img8.tif', 0) #original image

n_img = np.zeros((800,800))
final_img = cv.normalize(img,  n_img, 0, 255, cv.NORM_MINMAX)
#cv.imshow('Normalized Image', final_img)
#cv.imwrite('nr.jpg', final_img)

res = np.hstack((img, final_img)) #stacking images side-by-side
cv.imwrite('res.png',res)

    

