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

########################################### ADJUST HSV ########################################

# define the lower and upper boundaries of the colors in the HSV color space
#lower = {'colour':(0,210,70)} #assign new item lower['blue'] = (93, 10, 0)
#upper = {'colour':(40,255,255)}
 
# define standard colors for circle around the object
#colors = {'colour':(0,0,255)}

###############################################################################################
# 133 40 49
# 
lower = {'green':(15,160,100)}
upper = {'green':(60,255,255)}
colors = {'green':(45,200,150)}
###############################################################################################



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
        while not rospy.is_shutdown():
            (rval, frame) = ip_camera.stream.read()
            if rval:
                ip_camera.image_pub.publish(ip_camera.bridge.cv2_to_imgmsg(frame, "bgr8"))
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        ip_camera.stream.release()
        cv2.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass