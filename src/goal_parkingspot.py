#!/usr/bin/env python
import rospy
import roslib
import tf
from geometry_msgs.msg import PoseStamped, Point, Quaternion

def goal_parkingspot():
    


    
    pub = rospy.Publisher('move_base_simple/goal', PoseStamped)
    rospy.init_node('goal_parkingspot')
    coordinates = open('goalCoordinate.txt','r');
    px = float(coordinates.readline());
    py = float(coordinates.readline());
    pz = float(coordinates.readline());
    angle = float(coordinates.readline());
    
    current_time = rospy.get_rostime();
    #quaternion = tf.transformations.quaternion_from_euler(0,0,angle);
    goal_spot = PoseStamped();
    goal_spot.header.stamp = current_time;
    goal_spot.header.frame_id = "/map";
    #goal_spot.child_frame_id = "base_link";

    goal_spot.pose.position.x = px;
    goal_spot.pose.position.y = py;
    goal_spot.pose.position.z = pz;
    if angle==0:
	goal_spot.pose.orientation.x = 0;
	goal_spot.pose.orientation.y = 0;
	goal_spot.pose.orientation.z = -0;
	goal_spot.pose.orientation.w = 1;
    elif angle==180:
	goal_spot.pose.orientation.x = 0;
	goal_spot.pose.orientation.y = 0;
	goal_spot.pose.orientation.z = 1;
	goal_spot.pose.orientation.w = -0;
    elif angle==90:
	goal_spot.pose.orientation.x = 0;
	goal_spot.pose.orientation.y = 0;
	goal_spot.pose.orientation.z = 0.706;
	goal_spot.pose.orientation.w = 0.709;
    elif angle==-90:
	goal_spot.pose.orientation.x = 0;
	goal_spot.pose.orientation.y = 0;
	goal_spot.pose.orientation.z = -0.706;
	goal_spot.pose.orientation.w = 0.709;
		    
    #goal_spot.pose.orientation = quaternion;
    
    print goal_spot
    while not rospy.is_shutdown():
	pub.publish(goal_spot);
        rospy.sleep(1.0);

if __name__ == '__main__':
    try:
        goal_parkingspot()
    except rospy.ROSInterruptException:
        pass


