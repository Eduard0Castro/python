
def loop (repeticao: int) -> None:
    if repeticao > 0:
        print("Rodando")
        loop(repeticao-1)


loop(3)

#Fibonnaci:
def fibonnacci(posicao):

    n1 = 0 
    n2 = 1

    if posicao == 1:
        n3 = n1

    elif posicao > 1:
    
        for i in range(posicao-1):

            n3 = n1 +n2
            n1 = n2 
            n2 = n3

    print(n3)

fibonnacci(2)

def fibonnacci_recursivo(posicao: int) -> None:

    if posicao == 1:
        return 0

    if posicao == 2:
        return 1
    
    return fibonnacci_recursivo(posicao - 1) + fibonnacci_recursivo(posicao - 2)

print(fibonnacci_recursivo(2))




