cmake_minimum_required(VERSION 3.0.2)
project(robot_robot)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  geometry_msgs
  message_generation
  nav_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
  tf
)

generate_messages(DEPENDENCIES std_msgs)

generate_dynamic_reconfigure_options(cfg/robot.cfg)


catkin_package(
  CATKIN_DEPENDS 
  dynamic_reconfigure 
  geometry_msgs 
  message_runtime 
  roscpp 
  rospy 
  sensor_msgs 
  std_msgs 
  tf
)


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)


catkin_install_python(PROGRAMS
  scripts/odom_to_tf.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)