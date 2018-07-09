import cv2
import numpy as np
import math
inp_image = cv2.imread('red.jpg', 0)
Gray_Threshold = 127

def threshold(image=inp_image):
	mean  = image.mean()
	Standard_deviation = np.std(image) 
	Gray_Threshold = mean - 2*Standard_deviation
	ret,thresh_img = cv2.threshold(image, Gray_Threshold, 255, cv2.THRESH_BINARY)
	cv2.imwrite('im2.jpg', thresh_img)
	return thresh_img

threshold()