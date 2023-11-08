#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range

rospy.init_node('lidar')
lidar = Range()
def lidar_callback(sensor):
    global lidar
    lidar = sensor

sub_lidar = rospy.Subscriber("/mavros/distance_sensor/rangefinder_pub", Range, lidar_callback)

while not rospy.is_shutdown():
    altitude = lidar.range
    print(altitude)

    
