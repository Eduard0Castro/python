vector_ten = [float(input("Digite um numero real: ")) for x in range (5)]

for i in range(len(vector_ten), 0, -1):
    print(vector_ten[i-1])

print()
vector_ten.reverse()
for i in vector_ten:
    print(i)    
    