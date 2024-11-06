
def ReadInt(msg):

    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num)
            
        else:
            print("\033[31mErro, digite um número válido: \033[m")



def linha (tam = 42):
    print("-"*tam)

def menu(lista):
    linha()
    for pos, item in enumerate(lista):
        print(pos + 1, "-", item)
    linha()

    esc = ReadInt('Digite sua opção: ')
    return esc

