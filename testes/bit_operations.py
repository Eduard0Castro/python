data  = b'\x66' #01100110
data2 = b'\x04' #00000100
                #00111011
        #and     01000000


print("Valor inteiro em data: ", data[0])
print("Valor binario de data: ", bin(data[0]))

result = data[0] & data2[0] # or int.from_bytes
result = int.from_bytes(data, "big") & int.from_bytes(data2, "big")
print("AND operation between data and data2: ", hex(result))

if bool(result):print("EEPROM setting is finished")

resultado_x = (x & y for x, y in zip(data, data2) )
print(bytes(resultado_x).hex())

# Teste com valor de 23 bits com complemento de 2:

size = 23 # 24, mas último bit representa o sinal (complemento de 2)
teste = b'\x8f\x32\xd5'
mask  = b'\x80\x00\x00' # or bytes(1 << (size -1))

print("Valor testado: ", teste.hex())

teste_int = int.from_bytes(teste, "big")
mask_int  = int.from_bytes(mask,  "big")

#Testes para ver se é um numero negativo:
print(bool(teste_int & mask_int))
print(bool(teste_int >> size))

print(teste_int)
mask = (1 << size) - 1 # Mascara para quando fizer uma operação bitwise

real_value = -((~teste_int & mask) + 1) if teste_int >> size else teste_int

print(real_value)


#7392555

