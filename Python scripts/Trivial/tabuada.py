import time
import rospy
print ("Dê um valor")

valor = int(input('Valor:' ))
for num in range(1,11):
    print ('{} x {} = {}' .format(valor, num, valor*num))

time.sleep(1)

print('A potência é: {}' .format(valor**3))





