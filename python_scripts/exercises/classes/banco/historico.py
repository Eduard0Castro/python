
class Historico:
    def __init__(self):

        self.transacoes = []

    def imprime_extrato(self) -> None:
        for transacao in self.transacoes:
            print(transacao)


            
