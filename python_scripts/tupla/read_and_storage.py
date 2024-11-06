tupla = (int (input("Digite um número: ")),
         int(input("Digite outro número: ")),
         int(input("Digite mais um: ")),
         int(input("Digite o último agora: ")))

cont = 0
    
if 9 in tupla:
    cont += 1

print("\nO valor 9 apareceu {} vezes!" .format(cont))

if (3 in tupla):
    #index dessa forma pega o que a posição do 3 que aperece primeiro!        
    print("O primeiro número 3 foi digitado na {}ª posição" .format(tupla.index(3)+1))
else: 
    print("Nenhum número 3 foi digitado!")

print ("Os números pares digitados foram: ", end = '')
for i in range(0, len(tupla)):
    if (tupla[i]%2 == 0):
        print(tupla[i], end = ' ')

print("\n")