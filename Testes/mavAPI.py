import rospy
from mavros_msgs.srv import SetMode, CommandBool, CommandTOL, CommandHome, CommandLong, ParamSet
from mavros_msgs.msg import State, PositionTarget, GlobalPositionTarget, ParamValue
from std_msgs.msg import Float64, Int64
from geometry_msgs.msg import Twist, PoseStamped
from geographic_msgs.msg import GeoPoseStamped
from sensor_msgs.msg import NavSatFix, Range

from tadinisdk.control.mavros.scripts.gps_moviment import gps_send
from tadinisdk.control.mavros.scripts.geofence import Geofence
from tadinisdk.control.mavros.scripts.precision_land import PrecisionLand
class System:

    def __init__(self):

        # Declaração dos Subscribers:
        self._gps_sub = rospy.Subscriber('/mavros/global_position/global', NavSatFix, self._gps_callback)
        self._state_sub = rospy.Subscriber('/mavros/state', State, self._state_callback)
        self._rng_alt_sub = rospy.Subscriber('/mavros/distance_sensor/rangefinder_pub', Range, self._rng_alt_callback)
        self._rel_alt_sub = rospy.Subscriber('/mavros/global_position/rel_alt', Float64, self._rel_alt_callback)
        self._local_pos_sub = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, self._local_pos_callback)
        self._hdg_sub = rospy.Subscriber('/mavros/global_position/compass_hdg',Float64,self._hdg_callback)

        # Variáveis que serão utilizadas para Callbacks
        self._state = State()
        self._gps = NavSatFix() 
        self._rng_alt = Range()
        self._rel_alt = Float64()
        self._local_pos = PoseStamped()
        self._heading = Float64()


        # Wait Services:
        rospy.wait_for_service('/mavros/set_mode')
        rospy.wait_for_service('/mavros/cmd/arming')
        rospy.wait_for_service('/mavros/cmd/takeoff')   
        rospy.wait_for_service('/mavros/cmd/land')  
        rospy.wait_for_service('/mavros/cmd/set_home')
        rospy.wait_for_service('/mavros/param/set') 
        rospy.wait_for_service('/mavros/cmd/command')


        # Declaração dos Services:
        self._mode_srv = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        self._arm_srv = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        self._takeoff_srv = rospy.ServiceProxy('/mavros/cmd/takeoff', CommandTOL)
        self._land_srv = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
        self._home_srv = rospy.ServiceProxy('/mavros/cmd/set_home', CommandHome)
        self._param_set_srv = rospy.ServiceProxy('/mavros/param/set', ParamSet)
        self._command_srv = rospy.ServiceProxy('/mavros/cmd/command', CommandLong)

        # Declaração dos Publishers:
        self.gps_pub = rospy.Publisher('/mavros/setpoint_position/global', GeoPoseStamped, queue_size=1)
        self.gps2_pub = rospy.Publisher('/mavros/setpoint_raw/global', GlobalPositionTarget, queue_size=1)
        self.local_pub = rospy.Publisher('/mavros/setpoint_raw/local', PositionTarget, queue_size=1)

        self.delay(10)

    def _state_callback(self, data):
        self._state = data
    
    def _gps_callback(self, data): 
        self._gps = data

    def _rng_alt_callback(self, data):
        self._rng_alt = data

    def _rel_alt_callback(self, data):
        self._rel_alt = data

    def _local_pos_callback(self, data):
        self._local_pos = data

    def _hdg_callback(self, data):
        self._heading = data


    @property
    def get_state(self) -> State:
        """
        Return state data

        State
        ----------
        http://docs.ros.org/en/api/mavros_msgs/html/msg/State.html
        """
        return self._state 

    @property
    def get_gps(self) -> NavSatFix: 
        """
        Return gps data

        NavSatFix
        ----------
        http://docs.ros.org/en/api/sensor_msgs/html/msg/NavSatFix.html
        """
        return self._gps        

    @property
    def get_rel_alt(self) -> Float64:
        """
        Return relative altitude data from gps
        
        Float64
        ----------
        http://docs.ros.org/en/api/std_msgs/html/msg/Float64.html
        """
        return self._rel_alt

    @property
    def get_rng_alt(self) -> Range:
        """
        Return relative altitude data from lidar

        Range
        ----------
        http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Range.html
        """
        return self._rng_alt

    @property
    def get_local_pos(self) -> PoseStamped:
        """
        Return relative position data

        PoseStamped
        ----------
        http://docs.ros.org/en/api/geometry_msgs/html/msg/PoseStamped.html
        """
        return self._local_pos
    
    @property
    def get_heading(self) -> Float64:
        """
        Return heading data

        Float64
        ----------
        http://docs.ros.org/en/api/std_msgs/html/msg/Float64.html
        """
        return self._heading


    def _startup(self):
        self.initial_heading = self._heading.data
        self.initial_altitude = self._gps.altitude
        print(self.initial_altitude)
    

    def geofence(self, coords):
        """
        Create a polygon geofence, to get motors killed.

        Parameters
        ----------
        coords: List of lat ant long coordinates
        exemple: [(-22.41517936,-45.44797450),(-22.41493884,-45.44779748),(-22.41532317,-45.44727176)]
        """
        rospy.loginfo("-- Geofence created")
        Geofence(self, coords)
        


    def kill_motors(self):
        """
        Forced disarm
        
        Caution: it will disarm even during a flight
        """

        self._command_srv(0, 400, 0, 0, 21196, 0, 0, 0, 0, 0)    
        rospy.loginfo("-- Forced Disarm")


    def delay(self, time: float):
        """
        Send a dalay time 

        Parameters
        ----------
        time: float (seconds)
        """

        rospy.sleep(time)
        

    def set_mode(self, mode: str):
        """
        Modify the FCU flight mode.
        https://ardupilot.org/copter/docs/flight-modes.html

        Parameters
        ----------
        mode: strig (stabilize, alt_hold ,auto, guided, loiter, rtl, land, guided_nogps)
        """

        self._mode_srv(0, mode)
        rospy.loginfo("-- Mode " + mode.upper() + " was set")


    def arm(self):
        """
        Send command to arm the drone.
        """
        self.set_mode('GUIDED')
        self._startup()
        self._arm_srv(1)
        self.delay(3)
        rospy.loginfo("-- Arming")


    def takeoff(self, takeoff_alt: float):
        """
        Send command to take off and hold

        Parameters
        ----------
        takeoff_alt: float (meters)         
        """
        
        self._takeoff_srv(0, 0, 0, 0, takeoff_alt)
        rospy.loginfo("-- Takeoff Started")


    def arm_takeoff(self, takeoff_alt: float):
        """
        Send command to arm, take off and hold

        Parameters
        ----------
        takeoff_alt: float (meters)         
        """
        self.set_mode('GUIDED')
        self.arm()
        self.takeoff(takeoff_alt)


    def land(self):
        """
        Send command to land at the current position.
        """

        self._land_srv(0, 0, 0, 0, 0)
        rospy.loginfo("\033[1;32m-- Landing\033[m")


    def set_home(self, current_gps: bool, yaw=0.0, latitude=0.0 , longitude=0.0, altitude=0.0):
        """
        Change home position. Could be current position or a specified coordinates
        
        Parameters
        ----------
        current_gps: bool
            (True) Set current gps position

            (False) Enter the remaining parameters

        yaw: float32

        latitude: float32

        longitude: float32

        altitude: float32 
        """

        self._home_srv(current_gps, yaw, latitude, longitude, altitude)
        rospy.loginfo("-- Home set")


    def set_param(self, param_id: str, param_value: Int64):
        """ 
        Set the new parameter.

        Parameters
        ----------
        param_id: string: Name of the parameter that you want to change

        value: 
            integer: int64
            real: float64

        http://docs.ros.org/en/hydro/api/mavros/html/srv/ParamSet.html        
        """
        value = ParamValue()
        value.integer = param_value

        self._param_set_srv(param_id, value)
        rospy.loginfo("-- Parameter " + param_id.upper() + " was set to " + str(param_value))
   

    def rtl(self, rtl_alt, precisionland = False):
        """
        Send return to launch command.

        The copter will first rise to RTL_ALT before returning home or maintain the current altitude if the current altitude is higher than RTL_ALT. The default value for RTL_ALT is 15m.
        
        Parameters
        ----------
        rtl_alt: float (m)

        precisionland: boll (True or False)
        """
        altura = rtl_alt*100

        self.set_param('RTL_ALT', altura)
        self.delay(1)
        self.set_mode('rtl')
        if precisionland:
         PrecisionLand(self)

    def do_servo(self, aux_out, pwm_value):
        """
        Send a PWM signal to moviment a servo motor connected *aux_out*
        
        Parameters
        ----------
        aux_out: (int) auxiliar port, 1-6

        pwm_value: PWM value (usually between 1000 ~ 2000)       
        """
        aux_out = aux_out + 8

        self._command_srv(0, 183, 0, aux_out, pwm_value, 0, 0, 0, 0, 0)
    
    def offboard_gps_position(self, lat_setpoint, long_setpoint, alt_setpoint, heading, precision_radius):
        """
        Move sending a GPS coordinate
        
        Parameters
        ----------
        lat_setpoint: float

        long_setpoint: float

        alt_setpoint: float (meters AGL)

        heading: float (degrees refered to North)

        precision_radius: float (meters)
        """

        rospy.loginfo("-- Sending to GPS coordinates")
        gps_send(self, lat_setpoint, long_setpoint, alt_setpoint, heading, precision_radius)
        

    def offboard_local_position(self, position_x, position_y, position_z, yaw, ground_reference=True):
        """
        Move sending position commands. Move in a three dimentional space

        Parameters
        ----------
        position_x: float 

        position_y: float       

        position_z: float      

        yaw: float (degrees)

        ground_reference: Bool
            (True)Groud reference

            (False)Body reference
        """
        
        pose_msg = PositionTarget()

        if ground_reference:
            pose_msg.coordinate_frame = 1
        else:
            pose_msg.coordinate_frame = 8    

        pose_msg.type_mask = 2552 # 8+16+32+64+128+256+2048

        pose_msg.position.x = position_x
        pose_msg.position.y = position_y
        pose_msg.position.z = position_z
        pose_msg.yaw = yaw

        self.local_pub.publish(pose_msg)


    def offboard_velocity(self, linear_x: float, linear_y: float, linear_z: float, angular_z: float, ground_reference=True):
        """
        Move sending velocity commands

        Parameters
        ----------
        linear_x: float (m/s)
            (+)Move forward

            (-)Move backward 

        linear_y: float (m/s)      
            (+)Move left

            (-)Move right
        
        linear_z: float (m/s)     
            (+)Move up

            (-)Move down
        
        angular_z: float            
            (+)Rotate counter clockwise

            (-)Rotate clockwise

        ground_reference: Bool
            (True)Groud reference

            (False)Body reference
        """

        vel_msg = PositionTarget()

        if ground_reference:
            vel_msg.coordinate_frame = 1
        else:
            vel_msg.coordinate_frame = 8    

        vel_msg.type_mask = 1479 # 1+2+4+64+128+256+1024

        vel_msg.velocity.x = linear_x
        vel_msg.velocity.y = linear_y
        vel_msg.velocity.z = linear_z
        vel_msg.yaw_rate = angular_z

        self.local_pub.publish(vel_msg)


    def offboard_velocity_timer(self, linear_x=0, linear_y=0, linear_z=0, 
                                angular_z=0, ground_reference=True, pub_rate=30, time=0):
        """
        Move sending velocity commands and a time duration 

        Parameters
        ----------
        linear_x: float (m/s)
            (+)Move forward 

            (-)Move backward 

        linear_y: float (m/s)      
            (+)Move left

            (-)Move right
        
        linear_z: float (m/s)     
            (+)Move up          
            
            (-)Move down
        
        angular_z: float            
            (+)Rotate counter clockwise

            (-)Rotate clockwise

        ground_reference: Bool
            (True)Groud reference

            (False)Body reference

        pub_rate: uint (hertz)
            Publish rate on cmd_vel topic (30 Hz recommended)

        time: float (seconds)
            Moviment time duration 
        """

        t_start = t_now = rospy.get_rostime()
        duration = rospy.Duration(time)
        rate = rospy.Rate(pub_rate)

        rospy.loginfo("-- Moviment start")

        while t_now <= t_start + duration:

            self.offboard_velocity(linear_x, linear_y, linear_z, angular_z, ground_reference)
            rate.sleep()
            t_now = rospy.get_rostime()
