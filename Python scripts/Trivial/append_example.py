import time 
list = []
notas = int(input('QUantas notas serão aplicadas? '))
for i in range (0, notas):
    n = float(input(f'Digite o valor da nota {i+1}: '))
    list.append(n)

print(list)

