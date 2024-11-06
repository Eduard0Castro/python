num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))


for i in range(num1 + 1, num2, 1):
    print(i)

for i in range(num1 + 1, num2, 2):
    print(i)

for i in range(num2, num1 + 1, -1):
    print(i)
    
for i in range(num2, num1 + 1, -2):
    print(i)