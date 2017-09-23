import cv2
import numpy as np

"""
cv2.add is a 'saturated operation whiel numpy add is a modulo operation'
"""

def test_add():
    x=np.uint8([250])
    y=np.uint8([10])
    print("cv2.add:", str(cv2.add(x,y)))
    print("np  add:",str(x+y))


"""
Blending:
different kind of add:
different weights are given to images so that it gives a feeling of blending or transparency
"""
def test_Blending():
    img1=cv2.imread('ml.jgp')
    img2=cv2.imread('open_cv_logo.png')
    blending_img=cv2.addWeighted(img1,0.7,img2,0.3,0)
    cv2.imshow('image',blending_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_add()
    test_Blending()
