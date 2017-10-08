"""
Goal:
Concept of Canny edge detection

Theory:
Canny edge detection is a multi-stage algorithm:
1. Noise Reduction
    remove noise with 5x5 Gaussian filter
2. Finding intensity Gradient of the image
3. Non-maximum suppresion
4. Hysteresis Thresholding
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def test_canny():
    """
    cv2.canny
    argumetns:
    1. our input image
    2,3. min and max value for 'Hysteresis Thresholding'
    4. aperture_size, the size of sobel kernel used to find image gradient
    5. L2gradient, specify the equation for finding gradient magnitude.
    """
    img = cv2.imread('messi5.jpg', 0)
    edges = cv2.Canny(img, 100, 200)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('original image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge image'), plt.xticks([]), plt.yticks([])
    plt.show()
