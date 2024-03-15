from Testes.functions import Functions
import rospy

rospy.init_node('Teste')

move = Functions()

move.arm_takeoff(7)
move.delay(5)

move.frente_timer(1, 5)
move.delay(2)

move.esquerda_timer(1, 5)
move.delay(2)

move.direita_timer(1, 5)
move.delay(2)

move.tras_timer(1, 5)
move.delay(2)

move.land()