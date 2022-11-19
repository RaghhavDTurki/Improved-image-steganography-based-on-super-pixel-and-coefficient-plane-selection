from matplotlib.pyplot import imshow, figure, subplot, show, nipy_spectral, title
import matplotlib.cm as cm
import numpy as np
from PIL import Image
import dtcwt
from calc_superpixel import superpixel_mask


def loadImage(imagePath):
    im = Image.open(imagePath)
    return np.array(im)


def separateColorPlanes(image):
    # Separate the color planes: B, R, G
    B = image[:, :, 0]
    G = image[:, :, 1]
    R = image[:, :, 2]
    # Show image
    figure(1)
    subplot(2, 2, 1)
    imshow(image)
    subplot(2, 2, 2)
    imshow(B)
    subplot(2, 2, 3)
    imshow(G)
    subplot(2, 2, 4)
    imshow(R)
    show()
    return [B, G, R]


def dtcwtProcess(colorPLanes: list):
    transform = dtcwt.Transform2d()
    coeffs = []
    for image in colorPLanes:
        # Compute two levels of dtcwt with the defaul wavelet family
        Image_t = transform.forward(image, nlevels=2)
        # Show the absolute images for each direction in level 2.
        # Note that the 2nd level has index 1 since the 1st has index 0.
        # print("Image_t[1].shape: ", Image_t.highpasses[1].shape)
        print("DT-CWT coefficients for Color Plane: ", Image_t.highpasses[1])
        # coeffs.append(Image_t.highpasses[1])
        # figure(2)
        # for slice_idx in range(1,Image_t.highpasses[1].shape[2]):
        #     subplot(2, 3, slice_idx)
        #     imshow(np.abs(Image_t.highpasses[1][:,:,slice_idx]), cmap=nipy_spectral(), clim=(0, 1))
        # show()

        # Show the phase images for each direction in level 2.
        # figure(3)
        # for slice_idx in range(1,Image_t.highpasses[1].shape[2]):
        #     subplot(2, 3, slice_idx)
        #     imshow(np.angle(Image_t.highpasses[1][:,:,slice_idx]), cmap=cm.hsv, clim=(-np.pi, np.pi))
        # show()
    # Concatenate the coefficients into a single matrix
    finalCoeffs = np.concatenate(coeffs, axis=2)
    # print("Final Coeffs: ", finalCoeffs)
    return finalCoeffs


if __name__ == "__main__":
    # Load 1st image in the database
    image = loadImage(
        "/home/raghhav/iss_paper/never_compressed_images/uncompresseduncompressed_images/10001.bmp")
    colorPlanes = separateColorPlanes(image)
    dtcwtProcess(colorPlanes)
