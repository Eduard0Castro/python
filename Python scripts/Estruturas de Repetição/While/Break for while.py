n = 0
soma = 0
count = 0

while True:
    n = int(input("Digite um numero: "))

    if (n == 999):
        break

    count +=1
    soma += n

print(f"Foram digitados {count} números e a soma é {soma}")

