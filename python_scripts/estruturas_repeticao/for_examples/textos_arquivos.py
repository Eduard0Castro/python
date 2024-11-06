from pathlib import Path


path = Path().absolute().parent.parent.parent

nomes = ['Maria', 'Josefina', 'Maria Eduarda', 'Jovana', 'Julio']
idades = [12, 15, 50, 13, 44]

print("Nomes e idades listas: ")
for nome, idade in zip(nomes, idades, strict=True):
    print(f"{nome} tem {idade} anos")

dicio = {"Will": 15, "Whinderson": 13, "Carioca": 50, "Galgo":231}

print("\nNomes e idades dicionario: ")
for key, value in dicio.items():
    print(f"{key} tem {value}")

print("\nNomes do arquivo")
with open(f"{path}/Files/nomes.txt") as file:
    for n, linha in enumerate(file, start=1):
        print(f"{n} - {linha.strip()}")



