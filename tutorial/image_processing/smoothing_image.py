"""
2D covolution: image filtering
Low pass filter(LPF): help to remove noises
High pass filter(HPF): help to find edges

Question: how to get the kernel I want?
"""

import cv2
import matplotlib.pyplot as plt

"""
Image blurring: with LPF

1. Averaging
This is done by convolving image with a normalized box filter. It simply take
the average of all the pixel under the area and replace the central pixel.
"""
def test_Blur():
    img=cv2.imread('opencv-logo-white.png')
    blur=cv2.blur(img,(5,5))
    plt.subplot(121),plt.imshow(img),plt.title("original")
    plt.subplot(122),plt.imshow(blur),plt.title("blurred")
    plt.show()



"""
2. Gaussion blurring
gaussian kernel is used.

"""
def test_GaussianBlur():
    img=cv2.imread('opencv-logo-white.png')
    blur=cv2.GaussianBlur(img,(5,5),0)
    plt.subplot(121),plt.imshow(img),plt.title("original")
    plt.subplot(122),plt.imshow(blur),plt.title("blurred")
    plt.show()


"""
Median Blurring:
compare with average bluring, central pixel is replaced with median of pixel under
filter area.
"""
def test_MedianBlur():
    img=cv2.imread('opencv-logo-white.png')
    blur=cv2.medianBlur(img,5)
    plt.subplot(121),plt.imshow(img),plt.title("original")
    plt.subplot(122),plt.imshow(blur),plt.title("blurred")
    plt.show()


if __name__ == "__main__":
    # test_Blur()
    # test_GaussianBlur()
    test_MedianBlur()
