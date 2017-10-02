"""
paper: Rapid Object Detection using a Boosted Cascade of Simple Features
Intro:
It's a ML-based approach where a cascade function is trained from a lot of
positive and negtive images.

Pre-trainned classifier: opencv/data/haarcascades

"""

"""
API:
cv2.CascadeClassifier

parameters:
* scaleFactor:
    How much the image size is reduced at
    each image scale. This value is used to create the scale
    pyramid in order to detect faces at multiple scales
    in the image (some faces may be closer to the fore-
    ground, and thus be larger; other faces may be smaller
    and in the background, thus the usage of varying
    scales). A value of 1.05 indicates that Jeremy is re-
    ducing the size of the image by 5% at each level in the
    pyramid.
* minNeighbors:
    How many neighbors each window
    should have for the area in the window to be consid-
    ered a face. The cascade classifier will detect multiple
    windows around a face. This parameter controls how
    many rectangles (neighbors) need to be detected for
    the window to be labeled a face.
* minSize:
    A tuple of width and height (in pixels) in-
    dicating the minimum size of the window. Bounding
    boxes smaller than this size are ignored. It is a good
    idea to start with (30, 30) and fine-tune from there.
"""
