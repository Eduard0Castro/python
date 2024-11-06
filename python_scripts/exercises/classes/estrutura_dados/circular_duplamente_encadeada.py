from random import randint, choice
from time import sleep

class No:

    def __init__(self, num: int) -> None:
        self.num = num
        self.prox: No = None
        self.anterior: No = None

class Lista:

    def __init__(self):
        self.ini: No = None
        self.fim: No = None

    def insere(self, num: int) -> None:
            
        novo_no = No(num)

        if self.ini == None and self.fim == None:
            self.ini = novo_no
            self.fim = novo_no
            self.ini.prox = self.ini
            self.ini.anterior = self.ini

            return

        aux = self.ini

        while True:
            if aux.prox == self.ini or aux.prox.num > num:
                break
            aux = aux.prox
        
        if aux.prox == self.ini and aux.num < num: #último elemento
            aux.prox = novo_no
            novo_no.anterior = aux
            self.fim = novo_no
            novo_no.prox = self.ini
            self.ini.anterior = novo_no
                
        elif aux == self.ini and self.ini.num > num: #primeiro elemento
            self.ini.anterior = novo_no
            novo_no.prox = self.ini
            self.ini = novo_no
            self.fim.prox = novo_no
            self.ini.anterior = self.fim

        else:

            if aux == self.fim:
                novo_no.prox = self.fim
                novo_no.anterior = self.fim.anterior
                self.fim.anterior = novo_no

            else:
                novo_no.prox = aux.prox
                aux.prox = novo_no
                novo_no.anterior = aux
                novo_no.prox.anterior = novo_no

    def remover(self, num: int) -> None:
        aux = self.ini

        while aux.num != num: 
            aux = aux.prox

            if aux == self.fim and aux.num != num: 
                print("Não há esse numero na lista")

        if self.ini == aux: 
            self.ini = aux.prox
            self.ini.anterior = self.fim
            self.fim.prox = self.ini
            
            

        elif self.fim == aux:
            self.fim = aux.anterior
            self.fim.prox = self.ini
            self.ini.anterior = self.fim
            aux.anterior.prox = self.fim

        else:
            aux.anterior.prox = aux.prox
            aux.prox.anterior = aux.anterior


    def imprime(self) -> None:
        aux = self.fim

        while True:
            print(aux.num)
            sleep(1)
            if aux.anterior == self.fim: break
            aux = aux.anterior

def main():
    lista = Lista()
    guarda_num  = []

    for i in range(10):
        num = randint(0, 20)
        lista.insere(num)
        guarda_num.append(num)

    for num in guarda_num: lista.insere(num)

    lista.imprime()

    escolhido = 0
    print("\nPara remover: {}\n" .format(escolhido))
    lista.remover(escolhido)
    lista.imprime()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as Ki:
        pass


