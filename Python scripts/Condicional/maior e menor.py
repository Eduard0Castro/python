todos = []
n = 0
for i in range (1,4):
    n = int(input('Digite o numero {}: ' .format(i)))
    todos +=[n]

menor = todos[0]
maior = todos[0]

if todos[1] < todos[0] and todos[1] < todos[2]:
    menor = todos[1]
if todos [2] < todos [0] and todos [2] < todos [1]:
    menor = todos[2]
if todos[1] > todos[0] and todos[1] > todos[2]:
    maior = todos[1]
if todos [2] > todos [0] and todos [2] > todos [1]:
    maior = todos[2]

print(f'\n\033[31mO menor valor é o {menor}' )
print(f'\033[32mO maior valor é o {maior}' )


