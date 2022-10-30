
# GAMMA CORRECTION

import cv2 as cv
import numpy as np


def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv.LUT(src, table)


im = cv.imread('./pics/img6.tif', 0)
gammaImg = gammaCorrection(im, 2.2)

res = np.hstack((im, gammaImg)) #stacking images side-by-side
cv.imwrite('res.png',res)
