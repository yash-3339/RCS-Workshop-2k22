#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
if __name__=="__main__":
    try:
        rospy.init_node('Pub',anonymous=True)
        pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
        rate=rospy.Rate(10)
        vel=Twist()
        while not rospy.is_shutdown():
            vel.linear.x = 3
            vel.linear.y = 0
            vel.linear.z = 0
            vel.angular.x = 0
            vel.angular.y = 0
            vel.angular.z = 1
            rospy.loginfo("Cmd_vel Published")
            pub.publish(vel)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass