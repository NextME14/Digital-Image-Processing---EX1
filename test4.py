# -*- coding: utf-8 -*-


#adding salt and pepper to an image 

import cv2 as cv
import numpy as np

# 1) Open an original image 

img = cv.imread('./pics/img4.tif', 0)
img = img/255

# 2) Create a blank image 

x,y = img.shape

g= np.zeros((x,y), dtype=np.float32)

# 3) randomly filling the blank image 
 # salt and pepper amount 
pepper = 0.05
salt = 1 - pepper

#create salt and pepper noise image

for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img [i][j]
            
        # 5% pepper noise and 5% alt noise 
        
cv.imshow('image with noise', g)