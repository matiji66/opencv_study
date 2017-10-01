"""
What is histogram:
a graph or plot, gives you an overall idea about the intensity distribution
of an image. It is a plot with pixel values (range from 0 to 255) in X-axis and
corresponding number of pixels in the image on Y-axis.

Terminologies:
DIMS:
It is the number of the parameters for which we collect the data.
RANGE:
It is the range of the parameter value you want to measure.
"""

"""
cv2.calcHist()
 cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

1. images : it is the source image of type uint8 or float32. it should be given
    in square brackets, ie, “[img]”.
2. channels : it is also given in square brackets. It is the index of channel
    for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
3. mask : mask image. To find histogram of full image, it is given as “None”.
    But if you want to find histogram of particular region of image, you have to
    create a mask image for that and give it as mask. (I will show an example later.)
4. histSize : this represents our BIN count. Need to be given in square
    brackets. For full scale, we pass [256].
5. ranges : this is our RANGE. Normally, it is [0,256].

"""

import cv2
import os
from matplotlib import pyplot as plt

DATA_PATH= os.path.join(os.path.dirname(os.getcwd()),"data")

def calculateHist(filename):
    img=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    hist=cv2.calcHist([img],[0],None,[256],[0,256])
    #plot it
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    import pdb; pdb.set_trace()
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()

if __name__ == "__main__":
    calculateHist(os.path.join(DATA_PATH,"home.jpg"))
