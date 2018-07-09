import cv2
from threshold import threshold
from add_matrix import add_images
from resize_image import resize_image

im1 = cv2.imread('black.jpg', 0)
im2 = cv2.imread('red.jpg', 0)

print(im1.shape)

im1 = threshold(im1)
im2 = threshold(im2)

cv2.imwrite('im1.jpg', im1)
cv2.imwrite('im2.jpg', im2)

im1 = resize_image(im1)
im2 = resize_image(im2)

a = add_images(im1,im2)
cv2.imwrite('binary_image.jpg', a)