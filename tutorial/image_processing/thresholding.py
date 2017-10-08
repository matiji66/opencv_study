"""
If a pixel is greater than a value, then it assigned a one value.
else, it assigned another value.
cv2.threshold
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def test_threshold():
    img = cv2.imread('gradient.jpg', 0)
    ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()


def test_adaptivethreshold():
    img = cv2.imread('dave.jpg',0)
    img = cv2.medianBlur(img,5)

    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)
    import pdb; pdb.set_trace()
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()


def test_otsu_binarization():
    """
    In global thresholding, we used an arbitrary value for threshold value,
    right? So, how can we know a value we selected is good or not? Answer is,
    trial and error method. But consider a bimodal image (In simple words,
    bimodal image is an image whose histogram has two peaks). For that image,
    we can approximately take a value in the middle of those peaks as threshold
    value, right ? That is what Otsu binarization does. So in simple words, it
    automatically calculates a threshold value from image histogram for a bimodal image. (For images which are not bimodal, binarization won’t be accurate.)
    """
    pass
