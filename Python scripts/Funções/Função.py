def lin():
    print('-'*30)

def comp (write):

    lin()
    print(write)
    lin()

comp('Fernanda')
comp("A MALUCA")

def conta(a, b):
    s = a + b
    print(s)

conta(4,5)
conta(8,9)
conta(2,1)

#recebendo varios parâmetros: transformando em tupla!
def param (*num):
    print(num)
    size = len(num)
    print(f"{size} parâmetros recebidos!")

param (1,2,3,4,4,5,7,7,8,8)


soma = 0
hugo = list()
def read_list():
    global hugo
    while True:
        n = int(input(f"Digite um valor para colocar na lista 'hugo' (-1 para parar): "))
        if n == -1:
            break

        hugo.append(n)
read_list()

def print_list(lista):
    for i in range (0, len(lista)):
        print(lista[i], end=' ')
    print("")
print_list(hugo)