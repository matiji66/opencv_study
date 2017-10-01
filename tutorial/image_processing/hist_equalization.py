import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

"""
TODO:
* matho of Histogram equalization.
"""
"""
Theory:
adjust contrast of a image by using the image's histogram.

"""
DATA_PATH= os.path.join(os.path.dirname(os.getcwd()),"data")


def equalization_np(filename):
    img=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    hist,bins=np.histogram(img.flatten(),256,[0,256])
    cdf=hist.cumsum()
    cdf_normalized=cdf*hist.max()/cdf.max()
    plt.plot(cdf_normalized,color='b')
    plt.hist(img.flatten(),256,[0,256],color='r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'),loc='upper left')
    plt.show()

    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img2=cdf[img]
    plt.hist(img2.flatten(),256,[0,256],color='r')
    plt.xlim([0,256])
    plt.legend(('histogram'),loc='upper left')
    plt.show()


def equalization_cv(filename):
    img=cv2.imread(filename, cv2c.IMREAD_GRAYSCALE)
    equ=cv2.equalizeHist(img)
    # res=np.hstack((img,equ))
    cv2.imshow("image",equ)
    cv2.waitKey()
    cv2.destroryAllWindows()

"""
CLAHE(Contrast Limited Adaptive Histgram Equliaztion)
Motivation:
Normal equlization only consider global contrast of the image. some time this
will cause loss of information.
Theory:
Image is divided into small blocks called tiles. Then each of these blocks is
equalized as usual. BUT, if noise is there, it will be amlified. To avoid this,
contrast limiting is applied.
"""

def CLAHE_equlization(filename):
    img=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    cl1=clahe.apply(img)
    cv2.imshow("image",cl1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # equalization_np(os.path.join(DATA_PATH,"wiki.jpg"))
    # equalization_cv(os.path.join(DATA_PATH,'wiki.jpg'))
    CLAHE_equlization(os.path.join(DATA_PATH,'wiki.jpg'))
