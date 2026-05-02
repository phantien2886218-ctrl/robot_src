#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf
from nav_msgs.msg import Odometry

IMU_OFFSET_X = 0.0 
IMU_OFFSET_Y = 0.09
IMU_OFFSET_Z = 0.11  

def odom_callback(msg):
    br = tf.TransformBroadcaster()
    
    pos = msg.pose.pose.position
    ori = msg.pose.pose.orientation

    br.sendTransform(
        (pos.x, pos.y, pos.z),
        (ori.x, ori.y, ori.z, ori.w),
        msg.header.stamp,
        "base_footprint",
        "odom"
    )

    br.sendTransform(
        (IMU_OFFSET_X, IMU_OFFSET_Y, IMU_OFFSET_Z),
        (0.0, 0.0, 0.0, 1.0),
        msg.header.stamp,
        "imu_link",
        "base_footprint"
    )

if __name__ == '__main__':
    rospy.init_node('odom_tf_broadcaster_node')
    
    rospy.Subscriber('odom', Odometry, odom_callback)
    
    rospy.loginfo("Odom to TF Broadcaster (with IMU TF) is running...")
    rospy.spin()
