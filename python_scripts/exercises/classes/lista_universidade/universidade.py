from aluno import Aluno


class Universidade:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.qtd_alunos = 0
        self.prox: Universidade = None
        self.anterior: Universidade = None
        self.ini: Aluno = None
        self.fim: Aluno = None

    def insere(self, 
               nome: str, 
               matricula: int, 
               idade: int, 
               nro_disciplinas: int) -> None:
        nome = nome.capitalize()
        novo_no = Aluno(nome, matricula, idade, nro_disciplinas)


        if self.ini == None and self.fim == None:
            self.ini = novo_no
            self.fim = novo_no
            return

        aux = self.ini

        while True:
            if aux.prox == None or aux.prox.matricula > matricula:
                break
            aux = aux.prox

        if matricula == aux.matricula: 
            print("{} já está na lista" .format(nome))
            return
            
        if aux.prox == None and aux.matricula < matricula: #último elemento
            aux.prox = novo_no
            novo_no.anterior = aux
            self.fim = novo_no
                
        elif aux == self.ini and self.ini.matricula > matricula: #primeiro elemento
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

    def remover(self, matricula: int) -> None:
        

        aux = self.ini

        while aux.matricula != matricula: 


            if aux.prox == None and aux.matricula != matricula: 
                print(f"{matricula} não está na lista")
                return
            aux = aux.prox

        nome = aux.nome

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

        print(f"{nome} removido(a)")


    def imprime(self) -> None:
        print()
        aux = self.ini

        while True:
            print(aux.nome)
            if aux.prox == None: break
            aux = aux.prox

        print()

Universidade("UNIFEI")