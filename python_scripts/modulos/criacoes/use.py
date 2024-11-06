import python_scripts.modulos.criacoes.functions as functions

hugo = []
print(functions.factorial(5))

while True:
    n = int(input("Digite valores para a lista (-1 para sair): "))
    if n == -1:
        break
    hugo.append(n)

functions.vector(hugo)