"""
Draw geometric shapes with opencv
"""
import cv2
import numpy as np

"""
cv2.line(imge, pt1, pt2, color[,thickness[,lineType[,shift]]])
imge: image to paint
pt1: first point of line segmentation
pt2: second point of the line segmentation
color:
thickness:
lineStyle:
shift: ??
"""

def testLine():
    img=np.zeros((512,512,3),np.uint8)
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.imshow("mywin",img)
    cv2.waitKey()
    cv2.destroyAllWindows()



def testRectangle():
    img=np.zeros((512,512,3),np.uint8)
    cv2.rectangle(img,(384,0),(510,128),(255,0,0),5)
    cv2.imshow("mywin",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # testLine()
    testRectangle()
