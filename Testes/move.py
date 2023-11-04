from Functions import Functions
from mavAPI import System
import rospy
rospy.init_node('Teste')

move = Functions()
take = System()

take.arm_takeoff(7)
take.delay(5)

move.frente_timer(1, 5)
take.delay(2)

move.esquerda_timer(1, 5)
take.delay(2)

move.direita_timer(1, 5)
take.delay(2)

move.tras_timer(1, 5)
take.delay(2)

take.land()