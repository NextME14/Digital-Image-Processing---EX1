# GAMMA TRANSFORMATION

import cv2 as cv
import numpy as np

im = cv.imread('./pics/img7.tif', 0)

gamma = 2
im2 = np.power(im, gamma)

gamma = 3
im3 = np.power(im, gamma)

gamma = 4
im4 = np.power(im, gamma)

res = np.hstack((im, im2, im3, im4)) #stacking images side-by-side
cv.imwrite('res.png',res)


