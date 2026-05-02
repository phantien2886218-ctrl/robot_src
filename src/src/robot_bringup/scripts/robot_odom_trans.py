import roslib
import rospy
from   geometry_msgs.msg import PoseWithCovarianceStamped
from   nav_msgs.msg      import Odometry

class OdomTRANS():
    def __init__(self):
        
        rospy.init_node('odom_trans', anonymous=False)

        self.odom_pub = rospy.Publisher('output', Odometry,queue_size=10)
        
        rospy.wait_for_message('input', PoseWithCovarianceStamped)
        
        rospy.Subscriber('input', PoseWithCovarianceStamped, self.do_Msg)
        
        rospy.loginfo("Publishing combined odometry on /odom_trans")
        
    def do_Msg(self, msg):
        odom = Odometry()
        odom.header = msg.header
        odom.child_frame_id = 'base_footprint'
        odom.pose = msg.pose
        
        self.odom_pub.publish(odom)
        
if __name__ == '__main__':
    try:
        OdomTRANS()
        rospy.spin()
    except:
        pass

