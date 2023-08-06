res = int(input('Resistores: '))
volt = int(input('Voltagem: '))
valor = []
for i in range (0, res):
    print(i)
    n = str(input('Qual o valor do resistor {}? ' .format(i+1)))
    valor.append(n)

print(valor)

for j in range (1, volt+1):
    valor_2 = [volt]
    valor_2 [j] = float(input('Qual o valor da voltagem {}? ' .format(j)))


if (valor == 20 and valor_2 == 5):
        print('Vai te tomar no cu')






