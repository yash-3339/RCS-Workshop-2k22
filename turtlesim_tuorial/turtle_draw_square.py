#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__=="__main__":
    try:  
        rospy.init_node("square",anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        rate = rospy.Rate(100)
        vel= Twist()
        while not rospy.is_shutdown():
            vel.linear.x = 1
            vel.linear.y = 0
            vel.linear.z = 0
            vel.angular.x = 0
            vel.angular.y = 0
            vel.angular.z = 0
            pub.publish(vel)
            rate.sleep()
            vel.angular.z = 0
            vel.linear.x = 0
            pub.publish(vel)
            rate.sleep()
            vel.angular.z = 2
            vel.linear.x = 0
            pub.publish(vel)
            rate.sleep()
    except rospy.ROSInterruptException:pass
