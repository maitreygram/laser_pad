import numpy as np 
import cv2

def resize_image( image):
	# image_1 = cv2.imread(image)
	dim = (600,600)
	resized = cv2.resize(image , dim  , interpolation = cv2.INTER_LINEAR)
	return(resized)