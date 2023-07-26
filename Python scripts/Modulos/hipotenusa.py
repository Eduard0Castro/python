import math 
n = int(input('Digite o comprimento do cateto oposto: '))
n_2 = int(input('Digite o comprimento do cateto adjacente: '))

hipo = math.sqrt((math.pow(n,2))+ (math.pow(n_2,2)))
print(hipo) 