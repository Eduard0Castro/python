nome = "unkown"
preco = 0

soma = 0
cont = 0

contk = 0


while True:
    nome = str(input("Digite o nome do produto: ")).capitalize()
    preco = float(input("Digite o preço do produto: "))

    contk += 1

    if contk == 1:
        menor = preco
        n_menor = nome

    if preco < menor:
        menor = preco
        n_menor = nome


    soma += preco

    if preco > 1000:
        cont += 1


    stop = str(input("Quer parar?(S/N) ")).upper()
    if stop == "S":
        break
    
print("\nTotal gasto: R${}" .format(soma))
print("Produtos que custam mais de 1000: {}" .format(cont))
print(f"Produto mais barato: {n_menor}, R${menor}")

