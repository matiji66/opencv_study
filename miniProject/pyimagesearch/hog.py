from skimage import feature

class HOG(object):
    def __init__(self, orientation=9, pixelsPerCell=(8,8),
        cellsPerBlock=(3,3), transform=False):
        self.orientation=orientation
        self.pixelsPerCell=pixelsPerCell
        self.cellsPerBlock=cellsPerBlock
        self.transform=transform

    def describe(self, image):
        hist=feature.hog(image,
                orientations=self.orientation,
                pixels_per_cell=self.pixelsPerCell,
                cells_per_block=self.cellsPerBlock,
                transform_sqrt=self.transform)
        return hist
