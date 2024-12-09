from banco import Queue, Caixa
from threading import Thread
from random import randint
from time import sleep

def chegada(queue: Queue):
    for i in range(10):
        pessoa = f"Pessoa_{i}"
        queue.push(pessoa)
        print(f"Pessoa_{i} chegou para o atendimento")
        sleep(randint(3, 5))


def atendimento(queue: Queue):
    caixa1 = Caixa(12354, "Anailton")
    while True:
        sleep(randint(4, 7))
        pessoa = queue.pop()
        if pessoa: print(f"{pessoa.nome} foi para o atendimento com o caixa {caixa1.nome}")
        else: break


if __name__ == "__main__":

    queue = Queue()

    thread_chegada = Thread(target = lambda: chegada(queue))
    thread_atendimento = Thread(target = lambda: atendimento(queue))

    thread_chegada.start()
    thread_atendimento.start()

