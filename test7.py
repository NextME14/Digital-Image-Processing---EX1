#GAUSSIAN DENIOSING 

import cv2 as cv
import numpy as np


im = cv.imread('./pics/img20.tif', 0)



imm = cv.GaussianBlur(im, (7,7), 0, borderType = cv.BORDER_CONSTANT)

res = np.hstack((im, imm)) #stacking images side-by-side
cv.imwrite('res.png',res)