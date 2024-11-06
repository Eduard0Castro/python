soma = []

for i in range(1,4):
    seg = float(input('Digite o comprimento do segmento de reta {}: ' .format(i)))
    soma +=[seg]

maior = soma[0]
seg_1 = soma[1]
seg_2 = soma[2]
if soma[0] < soma[2] and soma[1]< soma[2]:
    maior = soma[2]
    seg_1 = soma[1]
    seg_2 = soma[0]

if soma[0] < soma [1] and soma[2] < soma [1]:
    maior = soma[1]
    seg_1 = soma[2]
    seg_2 = soma[0]

if (seg_1 + seg_2) > maior:
    print('\n\033[32mOs segmentos listados podem formar um triângulo!')

else:
    print('\n\033[31mOs segmentos listados não podem formar um triângulo!')