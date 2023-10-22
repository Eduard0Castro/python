def area(l, c):
    a = l*c
    print(f"A área do terreno {l}m x {c}m é {a}m²")

while True:
    l = float(input("Digite a largura do terreno: "))
    c = float(input("Digite o comprimento do terreno: "))
    area(l, c)

    f = ''
    while f != "N" and f != "S":
        f = str(input("Quer continuar? [S/N]: ")).upper()
    
    if f == 'N':
        break

