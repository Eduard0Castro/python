lados = [float(input("Digite o lado {}: " .format(x+1))) for x in range(3)]

tipo = str()
lados.sort(reverse=True)

if lados[0] < lados[1] + lados[2]:
    if lados[0] == lados[1] == lados[2]:
        tipo = "Equilátero"
    elif lados[0] != lados[1] != lados[2]:
        tipo = "Escaleno"
    else:
        tipo = "Isósceles"

    print(tipo)

else:
    print("Não pode ser um triângulo")




