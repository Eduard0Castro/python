q = int(input("Quantos números gostaria de colocar na lista? "))
todos = []

n = 0
for i in range (1,q+1):
    n = int(input('Digite o numero {}: ' .format(i)))
    todos +=[n]
print(todos)
menor = todos[0]
maior = todos[0]

for j in range (0, len(todos)):
    if todos[j] > maior:
        maior = todos[j]

    if todos[j] < menor:
        menor = todos[j]

print(f'\n\033[31mO menor valor é o {menor}' )
print(f'\033[32mO maior valor é o {maior}' )


