fisk = str()

def test_local():
    fisk = "Confuso sobrinho"
    return fisk

#Passagem de parâmetros é por referência, ou seja a função não altera o valor da variável passada
def second_test_local(value: str) -> str:
    value = "Madruginha"
    
    return value
    
# Não é uma boa prática alterar variáveis globais dessa forma dentro de funções:
def test_global():
    global fisk 
    fisk = 'Tião'

test_local()
print(fisk)

test_global()
print(fisk)

fisk = test_local()
print(fisk)

second_test_local(fisk)
print(fisk)
