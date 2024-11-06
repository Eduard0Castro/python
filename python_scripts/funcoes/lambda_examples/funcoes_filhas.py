
def dividir_por(num):
    return lambda x:x/num

# Váriavel recebe a função lambda:
dividir_por2 = dividir_por(2)
dividir_por3 = dividir_por(3)

print(dividir_por2(4))
print(dividir_por3(18))