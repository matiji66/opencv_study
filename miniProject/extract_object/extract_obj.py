import argparse
import math

import cv2
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument('-image', help='image to extract object from')


FLAGS = vars(ap.parse_args())

def main():
  image_org = cv2.imread(FLAGS['image'], cv2.IMREAD_COLOR)
  image_gray = cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY)
  # gaussion blur to remove noise
  image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)
  image_thresh = cv2.adaptiveThreshold(image_blur, 255,\
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                        cv2.THRESH_BINARY,
                                        11, 2)
  images = [image_gray, image_blur, image_thresh]
  titles = ['gray', 'blur', 'threshold']
  image_count = len(images)

  for i in range(image_count):
    plt.subplot(math.ceil(image_count/2), 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
  plt.show()




if __name__ == "__main__":
  main()
