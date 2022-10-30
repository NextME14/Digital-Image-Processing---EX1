# -*- coding: utf-8 -*-


#removing salt and pepper noise 

import cv2 as cv
import numpy as np

im = cv.imread('./pics/img20.tif', 0)
               
imm = cv.medianBlur(im, 3)    #using median filter 

im7 = cv.medianBlur(im, 7)

immm = cv.medianBlur(imm, 3) # use twice  of the same kernal     

#use mean filter 

im_mean = cv.filter2D(im, -1, np.ones((7,7))/49)     