hugo = []
while True:
    n = int(input("Digite um valor para a lista: "))
    if n in hugo:
        print("Número repetido, não adicionado!")
    else:
        hugo.append(n)

    c = "G"
    while c != "S" and c != "N":
        c = str(input("Quer continuar? [S/N]: ")).upper()

    if c != "S":
        break

hugo.sort()
print(hugo)