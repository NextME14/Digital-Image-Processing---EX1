#Implement a 2d spatial filter with python and compare it with conv2d filter 

# ImageFilter for using filter() function
from PIL import Image, ImageFilter


# Opening the image

# (R prefixed to string in order to deal with '\' in paths)
image = Image.open(r"./pics/img30.tif")

# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
image = image.filter(ImageFilter.GaussianBlur)

# Displaying the image
image.show()
#--------------
#USING FILTER2D OPTION

import cv2 as cv
import numpy as np

img = cv.imread('./pics/img30.tif', 0)

k = cv.getGaussianKernel(17, 3) #getting gaussian kernal
# 17*17 kernal in 2D

#(k*1) * (1*k) matrices
k2d = np.dot(k, k.T)

imgfilter2d = cv.filter2D(img, -1, k2d)
cv.imshow('filter2d method', imgfilter2d)

res = np.hstack((image, imgfilter2d)) #stacking images side-by-side
cv.imwrite('res.png',res)
