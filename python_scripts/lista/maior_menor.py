hugo = []
cont = 0
posb = posc = 0
for i in range (0, 5):
    hugo.append(int(input("Digite o numero para a posição {} na lista: " .format(i+1))))
    
    cont += 1

    if cont == 1:
        maior = hugo[i]
        menor = hugo[i]
    if hugo[i] <= menor:
        menor = hugo[i]
        posb = i + 1

    if hugo[i] >= maior:
        maior = hugo[i]
        posc = i + 1 

print(hugo)
print(maior, "-"*10, posc)
print(menor, "-"*10, posb)


