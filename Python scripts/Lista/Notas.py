hugo = []
nome = []
notas = []
princ = []

while True:
    nome.append(str(input("Nome: ")))
    notas.append(float(input("Nota 1: ")))
    notas.append(float(input("Nota 2: ")))
    
    media = (notas[0] + notas[1])/2

    notas.append(media)
    hugo.append(nome[:])
    hugo.append(notas[:])
    princ.append(hugo[:])

    nome.clear()
    notas.clear()
    hugo.clear()

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


