"""
Theory:
morphological transformation are some simple operation based on the image shape.
It needs 2 inputs, one is our original image, second one is called
<structuring element> or <kernel> which describe the nature of the operation.
"""
import cv2
import numpy as np

def org_imge_kernel():
    img = cv2.imread('morphological_j.png', 0)
    kernel = np.ones((5, 5), np.uint8)
    return img, kernel


def show_image(images):
    for k,v in images.items():
        cv2.imshow(k,v)
    cv2.waitKey()
    cv2.destroyAllWindows()

def test_erosion():
    """
    it enrods away the boundaries of foreground object(always try to keep foreground
    in white. The kernel slides through the image. A pixel in the original image,
    either 0 or 1) will be considered 1 only if all the pixels under the kenel
    is 1, otherwise it is erodes(made to 0)
    So what happens it that, all the pixels near boundary will be discarded
    depending upon the the size of kernel. So the thickness or size of the
    foreground object decreases or simply the white region decreases. It is useful
    for removing samll white noises, detach 2 connected objects etc.
    """
    img, kernel = org_imge_kernel()
    erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("erosion", erosion)
    cv2.imshow("original", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def test_dilation():
    """
    It just the opposite of erosion. A pixel is 1 if at least 1 pixel under the
    kernel is 1. So it increases the white region in the image or size of foreground
    object.
    """
    img, kernel = org_imge_kernel()
    dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imshow('original', img)
    cv2.imshow('dilationed', dilation)
    cv2.waitKey()
    cv2.destroyAllWindows()


def test_open_close():
    """
    Opending: another name of erosion followed by dilation. useful for removing
    noise
    Closing: reverse of opening, dialation followed by erosion. useful for Closing
    small holes inside the foreground objects.
    """
    img, kernel = org_imge_kernel()
    open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("original", img)
    cv2.imshow("open", open_img)
    cv2.imshow("close", close_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def test_morph_gradient():
    """
    It is the difference between dialation and erosion of an image
    The result will look like the outline of the object
    """
    img, kernel = org_imge_kernel()
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    show_image({"original":img, "gradient":gradient})


def test_tophat():
    """
    It is the difference between input image and opening image.
    """
    img, kernel = org_imge_kernel()
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    show_image({"original": img, "tophat": tophat})


def test_blackhat():
    """
    It is the difference between input image and closing image
    """
    img, kernel = org_imge_kernel()
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    show_image({"original": img, "blackhat":blackhat})


def test_get_structuring_element():
    """
    when you need other shape of kernel other than rectangular (eg, elliptical,
    circular). you can use this function: cv2.getStructuringElement(), just pass
    the shape and size, you can get desired kernel
    """
    print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
