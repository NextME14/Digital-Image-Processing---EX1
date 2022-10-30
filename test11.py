#LINEAR TRANSFORMATION

import cv2 as cv
import numpy as np

im = cv.imread('./pics/img1.tif', 0)

imb = np.zeros_like(im)
thresh = 50 #threshhold of intensity

#loops all the pixels in the image
for row in range (500): #loop along row
    for col in range (500): #loop along column
        #print(im[row, col])
        
#transform with T - like binarization
        if im[row, col] > thresh:
            imb[row, col] = 255

#real life senario
#numpy vectorization tech

imb2 = (im > thresh) 
imb2 = np.uint8(imb2)*255

#compare 3 images pixl by pixl

diff = np.abs(imb-imb2)
print('The maximum of difference is %lg.'%np.max(diff))