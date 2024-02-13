#!/usr/bin/env python3
import rospy
import tf2_ros
# import geometry_msgs.msg
# from geometry_msgs.msg import TransformStamped

def tf_callback(transform):
    # 这里假设transform.child_frame_id是物体的唯一标识符
    object_id = transform.child_frame_id
    position = transform.transform.translation
    orientation = transform.transform.rotation
    rospy.loginfo("Object ID: %s", object_id)
    rospy.loginfo("Position: \033[31mx=%.2f\033[0m, \033[32my=%.2f\033[0m, \033[34mz=%.2f\033[0m", position.x, position.y, position.z)
    rospy.loginfo("Orientation: x=%.2f, y=%.2f, z=%.2f, w=%.2f", orientation.x, orientation.y, orientation.z, orientation.w)
    rospy.loginfo("%------%")
def main():
    rospy.init_node('tf_listener_node')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(3.0)
    while not rospy.is_shutdown():
        try:

            for line in tfBuffer.all_frames_as_string().split('\n'):
                if f"with parent kinect2_rgb_optical_frame" in line:
                    # Extract the child frame name
                    # Note: This extraction depends on the specific format of the string.

                    child_frame = line.split(' ')[1]
                    if child_frame.startswith("object_"):
                        # rospy.loginfo("Attempting to look up transform for: %s", child_frame)  # Confirm it's attempting the lookup
                        transform = tfBuffer.lookup_transform('kinect2_rgb_optical_frame', child_frame, rospy.Time(0), rospy.Duration(1.0))
                        tf_callback(transform)
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            rospy.logwarn("TF error: %s", e)
        
        rate.sleep()

if __name__ == '__main__':
    main()
