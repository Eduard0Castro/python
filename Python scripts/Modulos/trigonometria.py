import math

angle = float(input('Digite o valor do angulo: '))
angle_1 = math.radians(angle)
sin = math.sin(angle_1)
cos = math.cos(angle_1)
tan = math.tan(angle_1)

print('O seno do angulo {} é: {:.2f} \nO cosseno do angulo {} é: {} \nA tangente do angulo {} é : {:.2f}' .format(angle, sin, angle, cos, angle, tan))


