include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,
  map_frame = "map",
  tracking_frame = "base_footprint", 
  published_frame = "odom",        
  odom_frame = "odom",
  provide_odom_frame = false,        
  publish_frame_projected_to_2d = false,
  use_pose_extrapolator = true,
  use_odometry = true,             
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
TRAJECTORY_BUILDER_2D.use_imu_data = false 
TRAJECTORY_BUILDER_2D.min_range = 0.1
TRAJECTORY_BUILDER_2D.max_range = 12.0
TRAJECTORY_BUILDER_2D.missing_data_ray_length = 5.
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true 

return options