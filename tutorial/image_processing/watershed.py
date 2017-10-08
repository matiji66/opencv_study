"""
Theory:

Any grayscale image can be viewed as a topographic surface where high intensity
denotes peaks and hills while low intensity denotes valleys. You start filling
every isolated valleys (local minima) with different colored water (labels).
As the water rises, depending on the peaks (gradients) nearby, water from
different valleys, obviously with different colors will start to merge.
To avoid that, you build barriers in the locations where water merges. You
continue the work of filling water and building barriers until all the peaks are
under water. Then the barriers you created gives you the segmentation result.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_image_and_wait(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)

def test_water_shed():
    img = cv2.imread('coins.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # find an approximate estimate of the coins
    # use Otsu's binarization
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    print("threshold is: {}".format(ret))
    cv2.imshow("thresh image", thresh)
    cv2.waitKey(0)

    # noise removal
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    cv2.imshow("remove noise", opening)
    cv2.waitKey(0)

    # sure backgroud area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    show_image_and_wait("sure background", sure_bg)

    # finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform,
                                 0.7*dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    show_image_and_wait("sure foreground", sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    show_image_and_wait("unknow", unknown)

    # marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers+1
    markers[unknown == 255] = 0
    show_image_and_wait("connected fg", markers)

    # water shed
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    show_image_and_wait("water shed", img)

    cv2.destroyAllWindows()
