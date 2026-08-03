"""

Com uma list comprehension, por exempĺo, de 10000 posições,
eu acabou salvando todos esses dados na minha memória.

Diferença entre iterator e generator: 

iterator trabalha com iteráveis (objetos que possuem o método __iter__)
iterator tem o método __iter__, que retorna ele mesmo, e o método __next__,
que faz a varredura como se fosse um ponteiro.
*Um iterador também é um iterável, mas nem sempre um iterável é um iterador

generator é uma função que consegue pausar sua execução
Permite declarar funções que se comportam como um iterator



Como pedir um valor de cada vez?


"""


# Exemplo:

import sys
from typing import Generator

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

# Notar que o tamanho da lista em bytes é muito maior que o do generator
# todos os elementos da lista já estão na memória
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# Using the generator pattern (an iterable)
class first_n(object):


    def __init__(self, n):
        self.n = n
        self.num = 0


    def __iter__(self):
        return self


    # Python 3 compatibility
    def __next__(self):
        return self.next()


    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        raise StopIteration()
  

generator = first_n(100000)
print(generator)
sum_of_first_n = sum(generator)
print(sum_of_first_n)

# Same as the class:

def first_n_function(n: int = 10) -> Generator:

    num = 0

    while num <= n:
        yield num # Pauso aqui toda vez. A cada next eu despauso meu loop e sigo para a próxima iteração
        num += 1

generator = first_n_function()
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))

# Same of everything:

generator = (n for n in range(10))



"""

Se eu chamo essa generator function com test(), 
não estou executando o conteúdo dessa função, mas 
retornando um generator capaz de lidar com as funcionalidades
e utilizar seus métodos nativos como 'next'

"""
# Generator functions tem o yield. 
def test() -> Generator:

    print("Tamo aí na generator function")

    yield 1
    #Notar que eu 'pauso' a execução da função
    print("Continuando ...")
    yield 2

teste = test() # Perceba que, ao chamar a função, nenhum print é executado
print(next(teste))
print(next(teste))



# Yield from

"""
É possível fazer com que um generator continue um outro generator.
Inicio um determinado gerador e termino com outro:

"""

def first_gen() -> Generator:

    for i in range(1, 4):
        yield i

def second_gen(gen: Generator) -> Generator:
    yield from gen
    yield 43

first = first_gen()
second = second_gen(first)


print()
print()
for i in second:
    print(i)
