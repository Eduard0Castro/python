""" 
Essa list comprehension vai travar porque vai gerar uma lista enorme que vai ocupar
toda a memória ram do computador:
 a = [i for i in range (600_000_000)]

Solução: geradores
    - vai gerar os valores a cada iteração:
"""
a = ( i for i in range (600_000_000))

"""
Para uma função como gerador, é possível utilizar a palavra reservada yield,    
que guarda o ponto de sua última chamada e gera o valor para cada iteração 
requisitada

"""
def generator(inicio = 0, limite = 10):
    
    n = inicio -1

    while True:

        if n >= limite:
            return
        
        n+=1
        yield n



a = generator(1, 10)

print("Primeira iteração")
for i in a:
    print(i)
    break

print("Segunda iteracao")
print(next(a))

print("Continução até 10: ")

for i in a:
    if i == 11:
        break
    print(i)



def chain(g1, g2):
    for i in g1():
        yield i

    print("\nOutro for: \n")
    for i in g2(1, 11):
        yield i


for i in chain(generator, generator):
    print(i)


print("\nForma cabaça: \n")

def chain2(g1: callable, g2: callable)-> None:
    for i in g1():
        print(i)

    print("\nSegundo for forma cabaça:")
    for i in g2(20, 35):
        print(i)

chain2(generator, generator)

linhas = 5
cols = 5

print("\nFor com gerador em tupla: ")
for linha, col in ((lin, col) for lin in range(linhas) for col in range(cols)):
    if linha == 4 and col == 3:
        print("OK!")
        break

def rows_cols(linhas: int, cols: int):
    for linha in range(linhas):
        for col in range(cols):
            yield (linha, col)

print("\nFor com gerador por função: ")

for linha, col in rows_cols(linhas, cols):
    if linha == 4 and col == 3:
        print(linha, col, "\nOK!")
        break

    



