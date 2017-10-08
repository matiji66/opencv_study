"""
Theory:
Contours can be explained simply as a curve joining all the continuous (along
the boundary), having same color or intensity.
* for better accuray, use binary images. beforef finding contures, aply threshold
or canny edge detection.

* in opencv, finding contours is like finding white object from black backgroud,
so object to be found should  be white and background should be black.

"""
import cv2


def test_simple_contour():
    img = cv2.imread('opencv-logo-white.png', 0)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    cimage, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, 0, [0, 255, 0], 3)
    cv2.imshow("contour", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def calc_contours():
    img = cv2.imread("star.jpg", 0)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    cimg, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    return contours
"""
Contour Features
"""
def test_moments():
    """
    image moments help you to calculate some features like center of mass,
    area of the object.
    """
    contours = calc_contours()
    cnt = contours[0]
    M = cv2.moments(cnt)
    print(M)


def test_contour_area():
    contours = calc_contours()
    area = cv2.contourArea(contours[0])
    print(area)


def test_contour_perimeter():
    contours = calc_contours()
    perimeter = cv2.arcLength(contours[0], True)
    print(perimeter)
