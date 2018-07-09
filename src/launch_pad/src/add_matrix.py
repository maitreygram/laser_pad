import cv2
import numpy as np 
import math
a = np.zeros((400,400,3))

def add_images(image_1=a, image_2=a):
	image_out = cv2.multiply(image_1,image_2)
	# image_out = image_out.astype(np.uint8)
	# ret,image_out = cv2.threshold(image_out, 127, 255, cv2.THRESH_BINARY_INV)
	return image_out