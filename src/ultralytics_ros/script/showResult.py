#!/usr/bin/env python

import rospy
from ultralytics_ros.msg import YoloResult

def callback(yolo_result):
    rospy.loginfo("Received a YoloResult message:")
    for detection in yolo_result.detections.detections:
        class_id = detection.results[0].id
        class_score = detection.results[0].score
        object_name = "Object ID: " + str(class_id) + "  Score: " + str(class_score)  # Replace with actual name mapping if available
        rospy.loginfo(object_name)

def listener():
    rospy.init_node('yolo_result_listener', anonymous=True)
    rospy.Subscriber("yolo_result", YoloResult, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()