import cv2
from threshold import threshold
from add_matrix import add_images
from resize_image import resize_image
import numpy as np

im1 = cv2.imread('im1.jpg', 0)
im2 = cv2.imread('im2.jpg', 0)

im1 = resize_image(im1)
im2 = resize_image(im2)
print(im1)
print(im2)
a = cv2.multiply(im1,im2)
print(a)

cv2.imwrite('binary_image.jpg', a)