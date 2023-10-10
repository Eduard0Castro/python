lista = [1, 2, 4, 3, 8, 6, 5, 6, 7, 9]

print("adicionar à última posição da lista: ")
lista.append(98)
print(lista)

print("lista organizada do maior para o menor:")
lista.sort(reverse = True)
print(lista)

print("inserir no endereço especificado e empurrar os outros elementos pra frente: ")
lista.insert(0, 133)
print(lista)

print("do menor para o maior e pop para remover o último:")
lista.sort()
lista.pop()
print(lista)

print("remove a primeira ocorrência do numero 6: ")
lista.remove(6)
print(lista)

print("inserindo de novo o seis na mesma posição anterior: ")
lista.insert(5, 6)
print(lista)

print("removendo todos os números 6 da lista: ")
while 6 in lista:
    lista.remove(6)
print(lista)

print("For diferente: ")
for pos, v in enumerate(lista):
    print(f"{pos}", "-"*10, f"{v}")

print(lista)

print("Fazendo uma ligação entre listas: ")
a = lista
a[0] = 9 #se eu mudo em uma, também mudo na outra
print(lista)
print(a)

print("Resolvendo: ")
b = a[:] #pegando os valores de a para b; Uma cópia de a!
b[0] = 333
print(a)
print(b)