from cliente import Cliente
from conta import Conta
from time import sleep

joaquim = Cliente("Joaquim", "890.764.360-90")
bb = Conta(144967, 17893, joaquim, 1000)

bb.saque(1000)
bb.deposito(1550.49)
bb.saque(550.90)
bb.saque(68.79)
bb.saque(123.98)

sleep(5.0)

bb.deposito(1200.90)
bb.saque(1300.50)

bb.extrato()