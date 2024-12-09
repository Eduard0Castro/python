from random import randint
from time import sleep

class Pessoa:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.prox: Pessoa = None

class Caixa(Pessoa):
    def __init__(self, matricula: int, nome: str) -> None:
        super().__init__(nome)
        self.matricula = matricula

class Queue:
   
    def __init__(self) -> None:
        self.fim: Pessoa = None
        self.ini: Pessoa = None

        
    def push(self, nome: str) -> None:
        nova = Pessoa(nome)

        if self.ini is None:
            self.fim = nova
            self.ini = nova
        
        else: 
            self.fim.prox = nova
            self.fim = nova

    def pop(self) -> Pessoa:

        if self.ini is not None:

            aux = self.ini
            self.ini = aux.prox
            return aux
        
        else: print("Fila vazia")


def main():
   
    dict_pessoa = {f"Pessoa_{i}": randint(3,5) for i in range(10)}
    caixa1 = Caixa(1234, "Silvano")
    queue = Queue()
    index = 0
    tempo_chegada = 0
    tempo_atendimento = randint(4,7)

    while True:

        if index < 10:

            if tempo_chegada == 0: 
                print(f"Pessoa_{index} chegou para o atendimento")
                queue.push(f"Pessoa_{index}")
                tempo_chegada = dict_pessoa.get(f"Pessoa_{index}")
                index += 1


            else: tempo_chegada -= 1

        if tempo_atendimento == 0: 
            tempo_atendimento = randint(4,7)
            pessoa = queue.pop()
            if pessoa is not None: print(f"{pessoa.nome} foi para o atendimento com o caixa {caixa1.nome}")
            else: break

        else:
            tempo_atendimento -= 1

        sleep(1)

   
if __name__ == "__main__":
   main()