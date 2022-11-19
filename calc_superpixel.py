# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
import cv2


def superpixel_mask(imagePath, numSegments=100):
    # load the image and convert it to a floating point data type
    image = cv2.imread(imagePath)
    image = img_as_float(image)
    # apply SLIC and extract (approximately) the supplied number
    # of segments
    segments = slic(image, n_segments=numSegments, sigma=5)
    # show the output of SLIC
    fig = plt.figure("Superpixels -- %d segments" % (numSegments))
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(image, segments))
    plt.axis("off")
    # show the plots
    plt.show()
    # load the image and apply SLIC
    # loop over the unique segment values
    for (i, segVal) in enumerate(np.unique(segments)):
        # construct a mask for the segment
        print("[x] inspecting segment %d" % (i))
        mask = np.zeros(image.shape[:2], dtype="uint8")
        mask[segments == segVal] = 255
        # show the masked region
        cv2.imshow("Mask", mask)
        cv2.imshow("Applied", cv2.bitwise_and(image, image, mask=mask))
        cv2.waitKey(0)
    return segments


superpixel_mask(
    "/home/raghhav/iss_paper/never_compressed_images/uncompresseduncompressed_images/10001.bmp")
