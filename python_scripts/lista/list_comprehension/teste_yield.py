
def teste_generator(inicio = 0, limite = 10):
    n = inicio
    while True:
        if n >= limite:
            return
        yield n
        n+=2

a = teste_generator()
for i in a:
    print(i)
    break

print("Pausa depois do primeiro for: \n")
for i in a:
    print(i)

    

def chain(g1, g2):

    for i in g1(0):
        print(i)

    for j in g2(1):
        print(j)

print("\nPrimeito chain: \n")
chain(teste_generator, teste_generator)



def chain2(g1, g2):
    for i in g1():
        yield i
    for j in g2(1):
        yield j


print("\nSegundo chain: \n")
for i in chain2(teste_generator, teste_generator):
    print(i)



def chain3(g1: callable, g2: callable):
    yield from g1 # delega a produção de valores para outro gerador
    yield from g2


print("\nTerceiro chain: \n")
teste = chain3(teste_generator(), teste_generator(1)) 
print(next(teste))
print(next(teste))
print(next(teste))
print(next(teste))

