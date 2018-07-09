#!/usr/bin/env python

import cv2,platform
import numpy as np
from sensor_msgs.msg import Image
import roslib
import sys
import rospy
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from collections import deque
import imutils
import urllib #for reading image from URL 
from threshold import threshold
from add_matrix import add_images
from resize_image import resize_image


###############################################################################################
class ipcamera(object):
    def __init__(self, url):
        try:
            self.stream=cv2.VideoCapture(url)
        except:
            rospy.logerr('Unable to open camera stream: ' + str(url))
            sys.exit() #'Unable to open camera stream')
        if not self.stream.isOpened():
            print "Error opening resource: " + str(url)
            print "Maybe opencv VideoCapture can't open it"
            sys.exit()
        #
        print "Correctly opened resource, starting to show feed."
        self.bytes=''
        self.image_pub = rospy.Publisher("ipcam10_vid", Image,queue_size=1000)
        self.bridge = CvBridge()
#	print 0

if __name__ == '__main__':
    try:
        camUrl='rtsp://192.168.0.112:5540/ch0'
        rospy.init_node('ipcam_10', anonymous=True)
        ip_camera = ipcamera(camUrl)
        output = np.zeros((600,600,3))
        # output = resize_image(output)
        while not rospy.is_shutdown():
            (rval, frame) = ip_camera.stream.read()
            if rval:
                # ADD CODE HERE
                # print(frame.shape)
                frame = resize_image(frame)
                # print(frame.shape)
                frame = threshold(frame)
                # print(frame.shape)
                # print('output image shape',output.shape)
                output = add_images(frame,output)

                ip_camera.image_pub.publish(ip_camera.bridge.cv2_to_imgmsg(frame, "bgr8"))
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        ip_camera.stream.release()
        cv2.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass