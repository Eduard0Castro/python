from time import sleep

def contagem(initial, fim, passo):

    if fim < initial:
        passo *= -1
    if passo == 0:
        if fim < initial:
            passo = -1
        elif passo == 0:
            passo = 1

    for i in range(initial, fim + passo, passo):
        
        print(f"{i} ", end='', flush = True)
        sleep(0.5)
    print('')

print("=-"*20)
initial = int(input("Digite o inicio da contagem agora: "))
fim = int(input("Digite aqui o fim da contagem: "))
passo = int(input("Digite o passo: "))
print("=-"*20)

print('Contagem com for: ')
contagem(0,10,1)
contagem(10, 0, 2)
contagem(initial, fim, passo)

def contagem_enquanto(initial, fim, passo):
    cont = initial
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    if fim < initial:
        while cont >= fim:
            print(cont, end = ' ', flush = True)
            sleep(0.5)
            cont -= passo

    else:
        while cont <= fim:
            print(cont, end = ' ', flush = True)
            sleep(0.5)
            cont += passo

    print("")
print("=-"*20)
print('Contagem com while: ')
contagem_enquanto(0,10,1)
contagem_enquanto(10, 0, 2)
contagem_enquanto(initial, fim, passo)
print("=-"*20)