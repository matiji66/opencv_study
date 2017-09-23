"""
Goals:
read, display, save image

Functions:
cv2.imread
cv2.imshow
cv2.imwrite
"""
import cv2

"""
cv2.imshow(filename[,flags])
filename: image file should be in the working directory or a full path
flags:
cv2.IMREAD_COLOR: load as a color image
cv2.IMREAD_GRAYSCALE: loads in grayscale mode
cv2.IMREAD_UNCHANGED: including alpha channel??
"""
img=cv2.imread("aloeR.jpg")
print(img.shape)



"""
cv2.imshow(winname, mat)
winname: name of windows that show the image
mat: images to show
"""
cv2.imshow("mywin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
cv2.imwrite(filename,image[,params])
filename: name of the file
image: image to be saved
params: format-specific parameters
"""

cv2.imwrite("saved_aloeR.jpg",img)
