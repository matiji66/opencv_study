import numpy as np
import cv2

"""
Target:
used for image segmentation for finding the objects of interest
in an image. In other word, it creates a image with same size(sigle channel)
as of our input image, where each pixel corresponds to he probability of that
pixel belongs to our object.

Action:
1. create a histogram of an image containing our object of interest.
2. back-project this histogram over our test image.
# """
