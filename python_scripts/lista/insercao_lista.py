hugo = list()

for i in range (0, 5):
    n = int(input("Digite um valor para colocar na lista: "))
   
    if i == 0 or n > hugo[len(hugo)-1]: #or hugo[-1]
        print("Adicionado a {}ª posição!" .format(i+1))
        hugo.append(n)
        

    for j in range (0, i+1): #i+1 para j chegar em todos os índices 
        if n < hugo[j]:
            hugo.insert(j, n)
            print("Adicionado a {}ª posição!" .format(j+1))
            break

print(hugo)
