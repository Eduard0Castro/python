from mavAPI import System 

drone = System()
class Functions():
    def esquerda(self, vel):
        """
            Send one velocity value for move left
        """

        drone.offboard_velocity(linear_y=abs(vel), ground_reference=False)

    def direita(self,vel):
        """
            Send one velocity value for move right
        """

        drone.offboard_velocity(linear_y=-abs(vel), ground_reference=False)

    def frente(self,vel):
        """
            Send one velocity value for move forward
        """

        drone.offboard_velocity(linear_x=abs(vel), ground_reference=False)

    def tras(self,vel):
        """
            Send one velocity value for move backward
        """

        drone.offboard_velocity(linear_x=-abs(vel), ground_reference=False)

    def cima(self,vel):
        """
            Send one velocity value for move up
        """

        drone.offboard_velocity(linear_z=abs(vel), ground_reference=False)

    def baixo(self,vel):
        """
            Send one velocity value for move down
        """

        drone.offboard_velocity(linear_z=-abs(vel), ground_reference=False)

    def yaw_horario(self,vel):
        """
            Send one velocity value for rotate clowise
        """

        drone.offboard_velocity(angular_z=-abs(vel), ground_reference=False)

    def yaw_antihorario(self,vel):
        """
            Send one velocity value for rotate counter clockwise
        """

        drone.offboard_velocity(angular_z=abs(vel), ground_reference=False)

    def esquerda_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move left 
        """
        
        drone.offboard_velocity_timer(linear_y=abs(vel), ground_reference=False, time = time)

    def direita_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move right
        """

        drone.offboard_velocity_timer(linear_y=-abs(vel), ground_reference=False, time = time)

    def frente_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move forward
        """
        
        drone.offboard_velocity_timer(linear_x=abs(vel), ground_reference=False, time = time)

    def tras_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move backward
        """
        
        drone.offboard_velocity_timer(linear_x=-abs(vel), ground_reference=False, time = time)

    def cima_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move up
        """
        
        drone.offboard_velocity_timer(linear_z=abs(vel), ground_reference=False, time=time)

    def yaw_horario_timer(self,vel, time):
        """
            Send one velocity value and a time duration for rotate clockwise
        """
        
        drone.offboard_velocity_timer(angular_z=-abs(vel), ground_reference=False, time= time)

    def yaw_antihorario_timer(self,vel, time):
        """
            Send one velocity value and a time duration for rotate counter clockwise
        """
        
        drone.offboard_velocity_timer(angular_z=abs(vel), ground_reference=False, time = time)

