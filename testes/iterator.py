"""
Sçao como ponteiros. Quando chegam a ultima posição, não conseguem mais executar
o método 'next', porque causa uma exceção de StopIteration. Isso acontece porque o ponteiro 
já aponta para a última posição.

O método 'iter' existe na classe dos 'iteráveis' também, que retorna um objeto iterator
que consegue lidar com meu iterável: geralmente chamando a próxima posição. 

"""

hugo = ['Thorzinho', 'Nina', 'Lilica', 'Bob']

iterator = iter(hugo)

print(iterator)


for i in range(0, 4):
    print(next(iterator))


class Teste:

    HUGO_TEST = ["Sloop", "Cremilda", "Spike", "Brauna"]

    def __iter__(self, ):

        return iter(Teste.HUGO_TEST)
    

test = Teste()
iterator = iter(test)
for i in range (0, 4):
    print(next(iterator))

