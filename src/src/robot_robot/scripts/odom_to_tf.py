#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf
from nav_msgs.msg import Odometry

# ================= 配置区域 =================
# 定义 IMU 相对于底盘中心 (base_footprint) 的安装位置
# 请根据你的实际安装修改这些值 (单位: 米)
IMU_OFFSET_X = 0.0 
IMU_OFFSET_Y = 0.09
IMU_OFFSET_Z = 0.11  

def odom_callback(msg):
    """
    回调函数：收到 /odom 话题数据时，将其转化为 TF 坐标变换广播出去
    同时广播 base_footprint -> imu_link 的静态变换
    """
    br = tf.TransformBroadcaster()
    
    # ---------------------------------------------------------
    # 1. 广播 odom -> base_footprint (动态变换)
    # ---------------------------------------------------------
    pos = msg.pose.pose.position
    ori = msg.pose.pose.orientation

    br.sendTransform(
        (pos.x, pos.y, pos.z),
        (ori.x, ori.y, ori.z, ori.w),
        msg.header.stamp,  # 使用 odom 消息的时间戳
        "base_footprint",  # 子坐标系
        "odom"             # 父坐标系
    )

    # ---------------------------------------------------------
    # 2. [新增] 广播 base_footprint -> imu_link (静态变换)
    # ---------------------------------------------------------
    # IMU 是固定在小车上的，所以我们发送一个固定的偏移量
    # 注意：这里使用 msg.header.stamp 确保两个 TF 在时间树上是对齐的
    br.sendTransform(
        (IMU_OFFSET_X, IMU_OFFSET_Y, IMU_OFFSET_Z), # 平移 (x, y, z)
        (0.0, 0.0, 0.0, 1.0),                       # 旋转 (x, y, z, w) - 这里设为无旋转 (0,0,0)
        msg.header.stamp,                           # 时间戳跟随 odom
        "imu_link",                                 # 子坐标系 (必须与 imu_data 消息里的 frame_id 一致)
        "base_footprint"                            # 父坐标系
    )

if __name__ == '__main__':
    rospy.init_node('odom_tf_broadcaster_node')
    
    # 订阅 Arduino 发布出来的 odom 话题
    rospy.Subscriber('odom', Odometry, odom_callback)
    
    rospy.loginfo("Odom to TF Broadcaster (with IMU TF) is running...")
    rospy.spin()