from statistics import mean
numbers = [float(input("Digite o numero {}: " .format(x+1))) for x in range(5)]

print("Soma dos valores: ", sum(numbers))
print("Media dos valores : ",  mean(numbers))


soma = 0
for i in numbers:
    soma += i

media = soma/len(numbers)

print(soma)
print(media)