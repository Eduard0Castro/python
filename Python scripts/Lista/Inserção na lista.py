hugo = list()
cont = 0
rep = 0
for i in range (0, 5):
    n = int(input("Digite um valor para colocar na lista: "))
    cont += 1
    if cont == 1:
        hugo.append(n)
        rep = n

    for j in range (0, i+1):
        if n < hugo[j]:
            hugo.insert(j, n)
            break

        elif j == i:
            hugo.append(n)
hugo.remove(rep)
print(hugo)
