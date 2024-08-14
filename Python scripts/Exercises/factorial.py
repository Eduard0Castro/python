
num = int(input("Digite um numero inteiro: "))
factorial = 1
for i in range (num, 0, -1):
    factorial *= i

print(factorial)