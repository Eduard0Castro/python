from cliente import Cliente
from historico import Historico
from datetime import datetime

class Conta:
    def __init__(self, numero:int, agencia: int, cliente: Cliente, saldo: float):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = saldo
        self.historico = Historico()


    def saque(self, value: float) -> None:

        if value > self.saldo:
            print("Valor informado ultrapassa o saldo")

        else:
            self.saldo -= value
            self.historico.transacoes.append(f"{datetime.today()}:    -{value}")
            print("Valor sacado com sucesso!")


    def deposito(self, value: float) -> None:
        self.saldo += value
        self.historico.transacoes.append(f"{datetime.today()}:    +{value}")
        print("Valor depositado com sucesso")

    def extrato(self):
        self.historico.imprime_extrato()

        