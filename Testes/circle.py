#!/usr/bin/env python3

import rospy
from mavAPI import System


class Circle(System):
    def __init__(self):
        super().__init__()
        rospy.init_node("circle")
        self.make_circle()
        
    def make_circle(self):
        self.arm_takeoff(7)
        self.delay(5)

        self.offboard_velocity_timer(linear_x=2, angular_z=3, ground_reference=False, time=20)
        self.offboard_velocity(linear_x=0,linear_y=0, linear_z=0, angular_z=0, ground_reference=False)

        self.delay(5)
        self.land()

if __name__ == "__main__":
    circle_node = Circle()
    

