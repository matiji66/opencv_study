"""
Target:
find image gradient, edge

Theory:
opencv provides 3 types of gradient filter or high-pass filter: Sobel, Scharr,
Laplacian.


Sobel: a joint Gaussion smoothing plus differentiation operation. So it is more
resistant to noise. you can specify the direction of derivatives to be taken:
vertical: y order
horizontal: x order

Laplacian:  it calculates the　Laplacian of the imag given by the relation.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("dave.jpg",0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2,2,1), plt.imshow(img, cmap="gray")
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian, cmap="gray")
plt.title('laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx, cmap="gray")
plt.title('sobelx'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely, cmap="gray")
plt.title('sobely'), plt.xticks([]), plt.yticks([])

plt.show()
