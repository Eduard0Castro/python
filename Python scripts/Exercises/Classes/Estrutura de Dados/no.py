from random import randint


class No():
    def __init__(self, num):
        self.num = num
        self.prox = None

class Lista():

    def __init__(self):
        self.ini = None

    def insere(self, num: int):
        novo_no = No(num)

        if self.ini == None:
            self.ini = novo_no
            return

        aux = self.ini

        while True:
            if aux.prox == None or aux.prox.num > num:
                break
            aux = aux.prox
        
        if aux.prox == None and aux.num < num: #último elemento
            aux.prox = novo_no
                
        elif aux == self.ini and self.ini.num > num: #primeiro elemento
            novo_no.prox = self.ini
            self.ini = novo_no
        else:
            novo_no.prox = aux.prox
            aux.prox = novo_no

    def imprime(self):
        aux = self.ini
        print("\n\n")
        while(True):
            print(aux.num)
            aux = aux.prox

            if aux == None:
                break

    def remover(self, value: int) -> None:
        aux = ant = self.ini

        while aux.num != value:
            ant = aux
            if aux.prox != None:
                aux = aux.prox

            elif aux.prox == None and aux.num != value:
                print("Não há esse numero na lista")
                return

        if aux == self.ini:
            self.ini = self.ini.prox
            print("Removendo inicio")

        elif aux.prox == None:
            ant.prox = None
            print("Removendo final")

        else:
            ant.prox = aux.prox
            print("Removendo meio")
        del aux


lista = Lista()

for i in range(5):
    lista.insere(randint(0, 10))

lista.imprime()