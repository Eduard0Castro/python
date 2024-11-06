mat = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
sot = 0
for i in range(0, 3):
    for j in range(0,3):
        mat[i][j] = int(input("Digite um numero para [{},{}]: " .format(i, j)))
        if mat[i][j]%2 == 0:
            soma += mat[i][j]

        if j == 2:
            sot += mat[i][j]

maiors = mat[1][0]

print("\nFormato de matriz: ")
for k in range(0, 3):
    for m in mat[k]:
        print(f"[{m}]", end="")

        if k == 1 and m > maiors:
            maiors = m
    
    print("")
    
print("A soma de todos os valores pares é:", soma)
print("A soma dos valores da coluna 3 é:",sot)
print("O maior valor da segunda linha é:", maiors)