hugo = []
par = []
impar = []
while True:
    hugo.append(int(input("Digite um numero para colocar na lista: ")))
    
    c = ""
    while c != "S" and c != "N":
        c = str(input("Quer continuar?[S/N]: ")).upper()

    if c == "N":
        break

for i in range (0, len(hugo)):
    if hugo[i]%2 == 0:
        par += [hugo[i]]
    else:
        impar += [hugo[i]]

print(f"Lista: {hugo}")
print("Pares: ", par)
print("Impares: ", impar)