#!/usr/bin/env python

import rospy
import sys
from geometry_msgs.msg import Twist

rospy.init_node('mov_velocidade', anonymous= False)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size= 10)
rate = rospy.Rate(10)

vel = Twist()

while not rospy.is_shutdown():
    vel.linear.x = -3
    #vel.linear.y = 0
    #vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0

    pub.publish(vel)
    rate.sleep()
