"""
Learn to handle mouse event in OpenCv
"""

import numpy as np
import cv2

"""
cv2.setMouseCallback(windowName, onMouse[,params])
windowName: window name to paint
onMouse: mouse callback
userdata: the optional parameter passed to the callback
"""

def ListAllEvent():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)


def testMouseCallback():
    # mouse click Function
    def draw_circle(event, x, y, flags, param):
        if event==cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img, (x,y),100,(255,0,0),-1)

    # create a black image, a windows and bind the callback function with windows
    img = np.zeros((512,512,3),np.uint8)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    while(1):
        cv2.imshow('image')
        if cv2.waitKey(20)&0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ListAllEvent()
    testMouseCallback()
