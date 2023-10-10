hugo=[]
cont = 0

while True:
    
    hugo.append(int(input("Digite um numero novo para a lista: ")))
    cont += 1

    n = ""
    while n != "N" and n != "S":
        n = str(input("Quer continuar?[S/N]: ")).upper()

    if n == "N":
        break

print("")
if 5 in hugo:
    print("Existe um 5 na lista!")
else:
    print("Não há nenhum 5 na lista!")

print("")
print(f"Foram digitados {cont} valores")
hugo.sort(reverse = True)
print(hugo)

