from pyimagesearch.eyetracker import EyeTracker
from pyimagesearch import imutils
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-f', '--face', required=True,
            help='path to where the face cascade resides')
ap.add_argument('-e', '--eye', required=True,
            help='path to where the eye cascade resides')
ap.add_argument('-i','--image', required=True,
            help='path to the image file')
args=vars(ap.parse_args())
et=EyeTracker(args['face'],args["eye"])

frame=cv2.imread(args['image'])

frame=imutils.resize(frame,width=300)
gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
rects=et.track(gray)
for rect in rects:
    cv2.rectangle(frame, (rect[0],rect[1]),
        (rect[2],rect[3]),(0,255,0),2)
cv2.imshow("Tracking", frame)
cv2.waitKey(0)

cv2.destroyAllWindows()
