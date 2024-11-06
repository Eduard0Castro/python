numeros = [1,2,3,4,5,6,7,8,2,7]

simple_square = [c**2 for c in numeros]
print(simple_square)

conditional_square = [d**2 for d in numeros if d**2 > 30]
print(conditional_square)