#Load images with opencv function into ipython environment

import cv2 as cv

#reading after splitting the image into 3 channels. 
im1 = cv.imread('./pics/img1.tif') 
im1b, im1g, im1r = cv.split(im1)

#reading as a gray image

im2 = cv.imread('./pics/img2.tif', 0)


