
class Lista:

    def __init__(self, tipo):
        self.ini = None
        self.fim = None
        self.Tipo = tipo

    def insere(self, nome: str) -> None:

        nome = nome.lower().capitalize()
        novo_no = self.Tipo(nome)


        if self.ini == None and self.fim == None:
            self.ini = novo_no
            self.fim = novo_no
            return

        aux = self.ini

        while True:
            if aux.prox == None or aux.prox.nome > nome:
                break
            aux = aux.prox

        if nome == aux.nome: 
            print("{} já está na lista" .format(nome))
            return
            
        if aux.prox == None and aux.nome < nome: #último elemento
            aux.prox = novo_no
            novo_no.anterior = aux
            self.fim = novo_no
                
        elif aux == self.ini and self.ini.nome > nome: #primeiro elemento
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

    def remover(self, nome: str) -> None:
        
        nome = nome.capitalize()

        aux = self.ini

        if aux:

            while aux.nome != nome: 

                if aux.prox == None and aux.nome != nome: 
                    print(f"{nome} não está na lista")
                    return
                
                aux = aux.prox


            if self.ini == aux: 
                self.ini = aux.prox
                if self.ini:
                    self.ini.anterior = None
                else: self.fim = None

            elif self.fim == aux:
                self.fim = aux.anterior
                self.fim.prox = None

            else:
                aux.anterior.prox = aux.prox
                aux.prox.anterior = aux.anterior

        else:
            print("Lista vazia, adicione elementos")


    def imprime(self) -> None:
        print()
        aux = self.ini

        while True:
            print(aux.nome)
            if aux.prox == None: break
            aux = aux.prox

        print()


def main():
    lista = Lista(Universidade)
    lista.insere("UNIFEI")
    lista.insere("Unicamp")
    lista.insere("USP")
    lista.insere("ITA")
    lista.insere("UNIFEI")
    lista.imprime()
    lista.remover("UNICAMPl")
    lista.remover("UNIFEI")
    lista.imprime()


if __name__ == "__main__":
    from universidade import Universidade
    main()
