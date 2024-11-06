def escreva(frase):
    size = len(frase)
    print("-"*size)
    print(frase)
    print("-"*size)

while True: 
    fr = str(input("Digite algo: "))
    escreva(fr)
    c = ''
    while c != "N" and c != "S":
        c = str(input("Quer continuar? [S/N]: ")).upper()

    if c == 'N':
        break