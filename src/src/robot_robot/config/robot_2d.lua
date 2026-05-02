include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,
  map_frame = "map",
  tracking_frame = "base_footprint", -- 追踪的坐标系
  published_frame = "odom",          -- 发布的父坐标系
  odom_frame = "odom",
  provide_odom_frame = false,        -- 因为你的 robot.launch 已经发布了 odom，这里设为 false
  publish_frame_projected_to_2d = false,
  use_pose_extrapolator = true,
  use_odometry = true,               -- 使用你的 Arduino 里程计
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 1,
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 0,
  lookup_transform_timeout_sec = 0.2,
  submaps_view_run_by_run = false,
  default_pose_graph_optimization_step_rescan_range = 10.,
  installation_directory = "../../",
  relative_odometry_max_distance_m = 0.1,
}

MAP_BUILDER.use_trajectory_builder_2d = true
TRAJECTORY_BUILDER_2D.use_imu_data = false -- 如果你暂时没有IMU，设为false
TRAJECTORY_BUILDER_2D.min_range = 0.1
TRAJECTORY_BUILDER_2D.max_range = 12.0
TRAJECTORY_BUILDER_2D.missing_data_ray_length = 5.
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true -- 关键：开启在线扫描匹配增强建图

return options