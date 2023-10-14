princ = []

while True:
    nome = (str(input("Nome: ")))
    nota1 = (float(input("Nota 1: ")))
    nota2 = (float(input("Nota 2: ")))
    media = (nota1 + nota2)/2

    princ.append([[nome], [nota1, nota2, media]])

    p = ""
    while p != "N" and p != "S":
        p = str(input("Quer continuar? [S/N]: ")).upper()

    if p == "N":
        break

print(princ)
print("\nNOTAS(média):")

for i in range (0, len(princ)):
    print(f"{i:<2}",f"{princ[i][0][0]}", f"{princ[i][1][2]:>10}")
    
print("")
while True:
    a = int(input("Mostrar notas de qual aluno?(-1 to stop!) "))
    if a == -1:
        break
    print(f"Notas de {princ[a][0][0]}: [{princ[a][1][0]}, {princ[a][1][1]}]\n")


