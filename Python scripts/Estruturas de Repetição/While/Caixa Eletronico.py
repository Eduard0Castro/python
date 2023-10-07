contc = 0
contv = 0
contd = 0
contu = 0
valor = 0
while True:
    saque = int(input("Qual o valor deseja sacar: "))
    
    if valor < saque:
        for i in range(valor, saque - 49, 50):
            valor += 50
            contc += 1
        for j in range(valor, saque - 19, 20):
            valor += 20
            contv += 1
        for k in range(valor, saque -9, 10):
            valor += 10
            contd += 1
        for l in range(valor, saque, 1):
            valor += 1
            contu += 1
    
    
    break

print(f"{contc} notas de 50\n{contv} notas de 20\n{contd} notas de 10\n{contu} notas de 1")
    

