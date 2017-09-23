"""
Simple application shows color you specify
* one window which show the color
* 3 trackbar
"""

"""
cv2.getTrackbarPos(trackbarname, windname)
reuturns: the current position of specified trackbar
"""

"""
cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
"""

import numpy as np
import cv2

def test_Trackbar():
    def nothing(x):
        pass
    img=np.zeros((300,512,3),np.uint8)
    cv2.namedWindow("image")

    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)

    switch='0:OFF\n1:ON'
    cv2.createTrackbar(switch,'image',0,1,nothing)

    while 1:
        cv2.imshow('image',img)
        if cv2.waitKey(20)&0xFF == ord('q'):
            break
        r=cv2.getTrackbarPos('R','image')
        g=cv2.getTrackbarPos('G','image')
        b=cv2.getTrackbarPos('B','image')
        s=cv2.getTrackbarPos(switch,'image')
        # import pdb; pdb.set_trace()
        if s:
            img[:]=[b,g,r]
        else:
            img[:]=0
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_Trackbar()
