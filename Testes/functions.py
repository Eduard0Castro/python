from mavAPI import System 

class Functions(System):
    def esquerda(self, vel):
        """
            Send one velocity value for move left
        """

        self.offboard_velocity(linear_y=abs(vel), ground_reference=False)

    def direita(self,vel):
        """
            Send one velocity value for move right
        """

        self.offboard_velocity(linear_y=-abs(vel), ground_reference=False)

    def frente(self,vel):
        """
            Send one velocity value for move forward
        """

        self.offboard_velocity(linear_x=abs(vel), ground_reference=False)

    def tras(self,vel):
        """
            Send one velocity value for move backward
        """

        self.offboard_velocity(linear_x=-abs(vel), ground_reference=False)

    def cima(self,vel):
        """
            Send one velocity value for move up
        """

        self.offboard_velocity(linear_z=abs(vel), ground_reference=False)

    def baixo(self,vel):
        """
            Send one velocity value for move down
        """

        self.offboard_velocity(linear_z=-abs(vel), ground_reference=False)

    def yaw_horario(self,vel):
        """
            Send one velocity value for rotate clowise
        """

        self.offboard_velocity(angular_z=-abs(vel), ground_reference=False)

    def yaw_antihorario(self,vel):
        """
            Send one velocity value for rotate counter clockwise
        """

        self.offboard_velocity(angular_z=abs(vel), ground_reference=False)

    def esquerda_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move left 
        """
        
        self.offboard_velocity_timer(linear_y=abs(vel), ground_reference=False, time = time)

    def direita_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move right
        """

        self.offboard_velocity_timer(linear_y=-abs(vel), ground_reference=False, time = time)

    def frente_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move forward
        """
        
        self.offboard_velocity_timer(linear_x=abs(vel), ground_reference=False, time = time)

    def tras_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move backward
        """
        
        self.offboard_velocity_timer(linear_x=-abs(vel), ground_reference=False, time = time)

    def cima_timer(self,vel, time):
        """
            Send one velocity value and a time duration for move up
        """
        
        self.offboard_velocity_timer(linear_z=abs(vel), ground_reference=False, time=time)

    def yaw_horario_timer(self,vel, time):
        """
            Send one velocity value and a time duration for rotate clockwise
        """
        
        self.offboard_velocity_timer(angular_z=-abs(vel), ground_reference=False, time= time)

    def yaw_antihorario_timer(self,vel, time):
        """
            Send one velocity value and a time duration for rotate counter clockwise
        """
        
        self.offboard_velocity_timer(angular_z=abs(vel), ground_reference=False, time = time)

