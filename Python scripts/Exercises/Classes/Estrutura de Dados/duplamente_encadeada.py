from random import randint, choice

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
            return

        aux = self.ini

        while True:
            if aux.prox == None or aux.prox.num > num:
                break
            aux = aux.prox
        
        if aux.prox == None and aux.num < num: #último elemento
            aux.prox = novo_no
            novo_no.anterior = aux
            self.fim = novo_no
                
        elif aux == self.ini and self.ini.num > num: #primeiro elemento
            self.ini.anterior = novo_no
            novo_no.prox = self.ini
            self.ini = novo_no
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

            if aux == None and aux.num != num: 
                print("Não há esse numero na lista")

        if self.ini == aux: 
            self.ini = aux.prox
            self.ini.anterior = None

        elif self.fim == aux:
            self.fim = aux.anterior
            self.fim.prox = None

        else:
            aux.anterior.prox = aux.prox
            aux.prox.anterior = aux.anterior

        


    def imprime(self) -> None:
        aux = self.fim

        while True:
            print(aux.num)
            if aux.anterior == None: break
            aux = aux.anterior

def main():
    lista = Lista()
    guarda_num = list()

    for i in range(10):
        num = randint(0, 20)
        lista.insere(num)
        guarda_num.append(num)

    lista.imprime()

    escolhido = choice(guarda_num)
    print("\nPara remover: {}\n" .format(escolhido))
    lista.remover(escolhido)
    lista.imprime()



if __name__ == "__main__":
    main()





