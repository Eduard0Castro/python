from time import time, sleep
#Criar um decorator para medir o tempo gasto em uma determinada função:

"""
O decorator é uma função que  precisa ter uma função "wrapper" que vai executar alguma outra funcionalidade 
aliada a execução da função passada. Se a função principal a ser executada pede argumentos, deve-se passar
os argumentos para a função wrapper que passará novamente para a função principal no momento em que ela está 
sendo executada.  
"""

def time_calculate(funcao: callable):
    def wrapper(* args):
        begin = time()
        result = funcao(* args)
        fim = time()
        print("Tempo gasto na função: {}" .format(fim - begin))
        return result
    return wrapper


@time_calculate
def calculate_tax(value: float) -> float:
    sleep(3)
    return value*0.2


print(calculate_tax(50.0))



