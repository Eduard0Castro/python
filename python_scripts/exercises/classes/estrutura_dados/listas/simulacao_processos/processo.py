from time import sleep

class Processo:

    def __init__(self, 
                 nome: str, 
                 prioridade: int, 
                 taxaCompleto: float, 
                 taxaPorCiclo: float, 
                 tempoProcessamento: float)-> None:
        
        self.nome = nome
        self.prioridade = prioridade
        self.taxaCompleto = taxaCompleto
        self.taxaPorCiclo = taxaPorCiclo
        self.tempoProcessamento = tempoProcessamento
        self.prox: Processo = None
        self.anterior: Processo = None

    @property
    def prioridade(self) -> int:
        return self._prioridade
    
    @prioridade.setter
    def prioridade(self, value: int) -> None:
        self._prioridade = max(0, min(5, value))


class ListaProcessos:
    def __init__(self):
        self.ini: Processo = None
        self.fim: Processo = None

    def insere(self, processo: Processo) -> None:
            
        novo_no = processo

        if self.ini == None and self.fim == None:
            self.ini = novo_no
            self.fim = novo_no
            self.ini.prox = self.ini
            self.ini.anterior = self.ini

            return

        aux: Processo = self.ini

        while True:
            if aux.prox == self.ini or aux.prox.prioridade > novo_no.prioridade:
                break
            aux = aux.prox
        
        if aux.prox == self.ini and aux.prioridade < novo_no.prioridade: #último elemento
            aux.prox = novo_no
            novo_no.anterior = aux
            self.fim = novo_no
            novo_no.prox = self.ini
            self.ini.anterior = novo_no
                
        elif aux == self.ini and self.ini.prioridade > novo_no.prioridade: #primeiro elemento
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

    def remover(self, processo: Processo) -> None:
        aux = self.ini

        while aux != processo: 
            aux = aux.prox

            if aux == self.fim and aux != processo: 
                print("Não há esse numero na lista")

        if self.ini == aux: 
            self.ini = aux.prox
            self.ini.anterior = self.fim
            self.fim.prox = self.ini
            

        elif self.fim == aux:
            self.fim = aux.anterior
            self.fim.prox = self.ini
            self.ini.anterior = self.fim


        else:
            aux.anterior.prox = aux.prox
            aux.prox.anterior = aux.anterior


    def imprime(self) -> None:
        aux = self.ini

        while True:
            print(aux.nome)
            sleep(1)
            if aux.prox == self.ini: break
            aux = aux.prox

    def run_process(self):
        aux = self.ini

        if aux:

            while True:

                aux.taxaCompleto += aux.taxaPorCiclo
                print(f"{aux.nome} entrou no processador")
                sleep(aux.tempoProcessamento)

                if aux.taxaCompleto >= 100:
                    print(f"{aux.nome} se encerrou")
                    self.remover(aux)
                
                    if aux == aux.prox: break

                else: print(f"{aux.nome} saiu do processador com taxa de {aux.taxaCompleto}%")

                aux = aux.prox
        else: print("Sem elementos na lista")


if __name__ == "__main__":
    process_list = ListaProcessos()
    proc1 = Processo("Processo 1", 1, 0, 20, 1)
    proc2 = Processo("Processo 2", 2, 0, 25, 2)
    proc3 = Processo("Processo 3", 5, 0, 30, 3)
    proc4 = Processo("Processo 4", 4, 0, 5,  1)
    proc5 = Processo("Processo 5", 3, 0, 50, 2)

    process_list.insere(proc1)
    process_list.insere(proc2)
    process_list.insere(proc3)
    process_list.insere(proc4)
    process_list.insere(proc5)

    process_list.run_process()

