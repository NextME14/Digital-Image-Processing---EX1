# Find edges and feature points from images

import cv2 as cv
import numpy as np

filename = './pics/img7.tif'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#img = cv.imread('./pics/img7.tif', 0)

gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv.imshow('dst',img)

#res = np.hstack((img, dst)) #stacking images side-by-side
#cv.imwrite('res.png',res)
