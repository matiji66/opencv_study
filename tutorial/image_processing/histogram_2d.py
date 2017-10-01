import numpy as np
import cv2
import sys
import os
from matplotlib import pyplot as plt

DATA_PATH= os.path.join(os.path.dirname(os.getcwd()),"data")

"""
Theory:
Compare to normal histogram, we consider 2 features. Normally it is
used to find color histogram, where 2 features are Hue & Saturation values
of every pixel.

Action:
1. convert image from BGR to HSV.
2. channels: [0,1]
3. bins:[180,256] 180 for H plane and 256 for S plane. accordingly,
range=[0,180,0,256]
"""

def test_2dhistogram(filename):
    img=cv2.imread(filename)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hist=cv2.calcHist([hsv],[0,1],None,[180,256],
                [0,180,0,256])
    print(hist.shape)
    # plt.plot(hist[0],color='r')
    # plt.plot(hist[1],color='b')
    # plt.show()
    plt.imshow(hist,interpolation='nearest')
    plt.show()

if __name__ == "__main__":
    test_2dhistogram(os.path.join(DATA_PATH,"home.jpg"))
