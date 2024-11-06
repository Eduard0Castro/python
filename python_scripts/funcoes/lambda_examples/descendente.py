notas = [('English', 8), ("Math", 10), ("History", 5.6), ("Portuguese", 9)]

notas.sort(key=lambda x:x[1], reverse=True)

print(notas)