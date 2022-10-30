#Do image enhancement especially edge enhance to ‘img7.tif’.

# import image module

from PIL import Image

from PIL import ImageFilter

 

# Open an already existing image

img = Image.open('./pics/img7.tif')

 

# Apply edge enhancement filter

edgeEnahnced = img.filter(ImageFilter.EDGE_ENHANCE)

 

# Apply increased edge enhancement filter

moreEdgeEnahnced = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

 

# Show original image - before applying edge enhancement filters

img.show() 

 

# Show image - after applying edge enhancement filter

edgeEnahnced.show()

 

# Show image - after applying increased edge enhancement filter

moreEdgeEnahnced.show()

import cv2 as cv
import numpy as np

res = np.hstack((img, edgeEnahnced, moreEdgeEnahnced)) #stacking images side-by-side
cv.imwrite('res.png',res)