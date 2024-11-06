dist = float(input('Digite a distancia entre o ponto de partida e o de chegada da sua viagem: '))

if dist <= 200:
    f = 0.5
    p = f*dist
    print('O preço da passagem é de {}' .format(p))

else:
    f = 0.45
    p = f*dist
    print('O preço da passagem é de {}' .format(p))

print(f)