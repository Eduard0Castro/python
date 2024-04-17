nomes = ["Marilou", "Eduardo", "Walter", "Julio", "Barbara", "Hugo"]

ordena = lambda x: sorted(x)

print(ordena(nomes))

print(nomes)

nomes.sort(key=lambda x:x[0])
print(nomes)