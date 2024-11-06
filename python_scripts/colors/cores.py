#    1 vermelho = '\033[31m'
#    2 verde = '\033[32m'
#    3 azul = '\033[34m'
#    4 
#    5 ciano = '\033[36m'
#    6 magenta = '\033[35m'
#    7 amarelo = '\033[33m'
#    8 preto = '\033[30m'
#    9 
#   10 branco = '\033[37m'
#   11 
#   12 restaura cor original = '\033[0;0m'
#   13 negrito = '\033[1m'
#   14 reverso = '\033[2m'
#   15 
#   16 fundo preto = '\033[40m'
#   17 fundo vermelho = '\033[41m'
#   18 fundo verde = '\033[42m'
#   19 fundo amarelo = '\033[43m'
#   20 fundo azul = '\033[44m'
#   21 fundo magenta = '\033[45m'
#   22 fundo ciano = '\033[46m'
#   23 fundo branco = '\033[47m'

cores  = {'vermelho':'\033[31m', 'verde':'\033[31m', 'azul':'\033[34m' , 'amarelo':'\033[33m'}

c = ('\033[m',   #0 - sem cor
     '\033[31m', #1 - vermelho 
     '\033[32m', #2 - verde
     '\033[33m', #3 - amarelo
     '\033[34m', #4 - azul
     '\033[35m', #5 - magenta
     '\033[36m') #6 - ciano

print(f"{c[2]}Olá{c[0]} Eduardo")