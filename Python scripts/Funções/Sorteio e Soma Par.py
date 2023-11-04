from random import randint
def sorteio():
    hugo = list()
    for i in range (0, 5):
        hugo += [randint(0, 5000)]
        
    print (hugo)

    return hugo

def somaPar(lista):
    soma = 0 
    size = len(lista)
    for i in range (0, size) :
        if (lista[i]%2 == 0):
            soma += lista[i]
            print(lista[i], end=' ')

    print(f"\nA soma dos pares é: {soma}")


kiko = sorteio()
somaPar(kiko)