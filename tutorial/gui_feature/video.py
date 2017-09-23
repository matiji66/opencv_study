"""
Playing a video from filename
"""

import cv2
import os

VIDEO_FILE= "/home/scott/github/opencv_study/pycv-master/first_edition/chapter2/miscellaneous/MyInputVid.avi"

def testVideoCapture():
    cap = cv2.VideoCapture(VIDEO_FILE)

    if cap.isOpened():
        ret,frame=cap.read()
        while ret:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("frame",gray)
            ret,frame=cap.read()
            if cv2.waitKey(10)&0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()


"""
Properties of VideoCapture:
"""


"""
VideoWriter:
filename: Name of output file
fourcc: 4-character code of codec used to compress the frames.
fps: Framerate of the created video stream
framesize: Size of the vide frames
isColor: if not zero, the encoder will expect and encode color frames, otherwise,
it will work with grayscale.
"""

CURRENT_DIR=os.getcwd()

def testVideoWriter():
    source=cv2.VideoCapture(VIDEO_FILE)
    fourcc=cv2.VideoWriter_fourcc(*'MJPG')
    dist=cv2.VideoWriter("outputvide.avi",fourcc,5,(640,480))
    if source.isOpened():
        ret,frame=source.read()
        while ret:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("mywin",gray)
            cv2.waitKey(10)
            dist.write(frame)
            ret,frame=source.read()
    source.release()
    dist.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    testVideoWriter()
