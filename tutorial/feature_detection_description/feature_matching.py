"""
Basics of Brute-Force Matcher:
It takes the descriptor of one feature in the first set and
is matched with all other feature in second set using some **distance calculation**
and the closest is returned.

BF matcher: cv2.BFMatcher
args:
    normType: it specifies the distance measurement to be used
        cv2.NROM_L2: SIFT, SURF
        cv2.NORM_HAMMING: ORB, BRIEF, BRISK (binary based descriptor)
    crossCheck:
        True:

"""
import cv2
from matplotlib import pyplot as plt



img1 = cv2.imread('box.png',0)          # queryImage
img2 = cv2.imread('box_in_scene.png',0) # trainImage

# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)

plt.imshow(img3),plt.show()

"""
Mathcer object:
the match method of BFMatcher return a list a DMatch objects.
The DMatch object has following attributes:
1. DMatch.distance: distance between discriptors. the lower, the better.
2. DMatch.trainIdx: index of the descriptor in train descriptor
3. DMatch.queryIdx: index of the descriptor in the query descriptor
4. DMatch.imgIdx: Index of the train image
"""


"""
FLANN: Fast Library for Aproximate Nearest Neighbors.
it contains a collection of algorithms optimized for fast nearest neighbor search
in large datasets and for high dimentional features.
"""
