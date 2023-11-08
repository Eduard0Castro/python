from Interface.library import *
from Interface.file import *


arq = 'names.txt'

if fileexist(arq) is not True:
    
    createfile(arq)


while True:
    esc = menu(['Cadastrar qualquer coisa', 'Visualizar cadastros', 'Sair do Sistema'])
    if esc == 1:
        try:
            name = str(input("Digite o nome: "))
            idade = int(input("Idade: "))
        except(ValueError):
            print("\n\033[31mIsso não funcionou, tente de novo!\033[m")
        else:
            writefile(arq, name, idade)
    elif esc == 2:
        print("Cadastros: ")
        readfile(arq)

    elif esc == 3:
        print("Saindo")
        break
    else:
        print("\033[31mDigite um número dentro das opções!!!\033[m")


              
