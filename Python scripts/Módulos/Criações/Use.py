import Functions

hugo = []
print(Functions.factorial(5))

while True:
    n = int(input("Digite valores para a lista (-1 para sair): "))
    if n == -1:
        break
    hugo.append(n)

Functions.vector(hugo)