"""
Theory:
There are 2 kinds of image pyramids:
1) Guassian pyramid

2) Laplacian Pyramid
Laplacian Pyramids are formed from the Gaussian.
Laplacian pyramid are like edge images only.
"""
import cv2
import numpy as np

def test_gaussian_pyramid():
    """
    remove consecutive rows and columns in lower level. Then each
    pixel in higher level is formed by the contribution from 5 pixels
    in underlying level with gaussian weights. By doing so, M x N image
    become M/2 x N/2.
    """
    img = cv2.imread('messi5.jpg')
    lower_reso = cv2.pyrDown(img)
    higher_reso = cv2.pyrUp(img)
    lower_then_higher = cv2.pyrUp(lower_reso)
    cv2.imshow("original", img)
    cv2.imshow("lower", lower_reso)
    cv2.imshow("higher", higher_reso)
    cv2.imshow("lower then higher", lower_then_higher)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_image_blending():
    """
    when we want stack 2 images, it may not look good due to discontinuities
    between images. image blending with Pyramids gives you seamless blending
    without leaving much data in the images.
    """
    A = cv2.imread('apple.jpg')
    B = cv2.imread('orange.jpg')

    # generate Gaussian pyramid for A
    G = A.copy()
    gpA = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpA.append(G)

    # generate Gaussian pyramid for B
    G = B.copy()
    gpB = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpB.append(G)

    # generate Laplacian Pyramid for A
    lpA = [gpA[5]]
    for i in range(5,0,-1):
        GE = cv2.pyrUp(gpA[i])
        L = cv2.subtract(gpA[i-1],GE)
        lpA.append(L)

    # generate Laplacian Pyramid for B
    lpB = [gpB[5]]
    for i in range(5,0,-1):
        GE = cv2.pyrUp(gpB[i])
        L = cv2.subtract(gpB[i-1],GE)
        lpB.append(L)

    # Now add left and right halves of images in each level
    LS = []
    for la,lb in zip(lpA,lpB):
        rows,cols,dpt = la.shape
        ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
        LS.append(ls)

    # now reconstruct
    ls_ = LS[0]
    for i in range(1,6):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(ls_, LS[i])

    # image with direct connecting each half
    real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

    cv2.imshow("pyramid blending", ls_)
    cv2.imshow("direct blending", real)
    cv2.waitKey()
    cv2.destroyAllWindows()
