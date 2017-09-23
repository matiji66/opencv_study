import cv2
import numpy as np

"""
scalling:
cv2.resize
interpolation:
INTER_NEAREST: nearest neighbor interpolation
INTER_LINEAR: bilinear interpolation
etc,
"""

def test_warpAffine():
    img=cv2.imread('messi5.jpg',0)
    rows, cols = img.shape
    M=np.float32([[1,0,100],[0,1,50]])
    dst=cv2.warpAffine(img,M,(cols,rows))

    cv2.imshow("imge",dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

"""
Rotation:
besides normal rotation:
OpenCV provides scaled rotation with ajustable enter of ratotation. so that you
can rotation at any location you prefer.
"""

"""
firstly, find the rotation matrix:

cv2.getRotationMatrix2D(center, angle, scale)
center: center of rotation
angle: rotation angle. Positive counter mean counter-clockwise rotation
"""

def test_Rotation():
    img=cv2.imread('messi5.jpg',0)
    rows, cols=img.shape
    # get rotation matrix
    M=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst=cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('image',dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def test_affineTransformation():
    img = cv2.imread('drawing.png')
    rows,cols,ch = img.shape
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv2.getAffineTransform(pts1,pts2)
    dst = cv2.warpAffine(img,M,(cols,rows))
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')

if __name__ == "__main__":
    # test_warpAffine()
    test_Rotation()
