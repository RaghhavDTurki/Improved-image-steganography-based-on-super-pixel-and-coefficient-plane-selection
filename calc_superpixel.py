# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
import cv2

# load the image and apply SLIC and extract (approximately)
# the supplied number of segments
image = cv2.imread("C:/Users/raghh/PYTHON/iss_paper/never_compressed_images/uncompresseduncompressed_images/10002.bmp")
segments = slic(img_as_float(image), n_segments = 100, sigma = 5)
print(segments)
# show the output of SLIC
fig = plt.figure("Superpixels")
ax = fig.add_subplot(1, 1, 1)
ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments))
plt.axis("off")
plt.show()
# loop over the unique segment values
# for (i, segVal) in enumerate(np.unique(segments)):
# 	# construct a mask for the segment
# 	print ("[x] inspecting segment %d" % (i))
# 	mask = np.zeros(image.shape[:2], dtype = "uint8")
# 	mask[segments == segVal] = 255
# 	# show the masked region
# 	cv2.imshow("Mask", mask)
# 	cv2.imshow("Applied", cv2.bitwise_and(image, image, mask = mask))
# 	cv2.waitKey(0)