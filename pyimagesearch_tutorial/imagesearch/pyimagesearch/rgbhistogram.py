import numpy as np
import cv2

class RGBHistogram(object):
    def __init__(self,bins):
        self.bins=bins

    def describe(self,image):
        #calculate a 3D histogram in the RGB colorspace
        #then normalize the histogram so that the images
        #with the same color content, but either scaled larger
        # or smaller will have the same histogram
        hist=cv2.calcHist([image],[0,1,2],
                        None,self.bins,[0,256,0,256,0,256])
        hist=cv2.normalize(hist,hist)
        return hist.flatten()
