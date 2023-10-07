idade = 0
sexo = 'Male'
conti = 0
conth = 0
contm = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M/F): ')).upper()
    if idade > 18:
        conti +=1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1

    stop = str(input('\nDigite se gostaria de continuar: (S/N)')).upper()

    if stop == 'N':
        break
  

    
print ("\nA quantidade de pessoas com mais de 18 anos é {}" .format(conti))
print("A quantidade homens cadastrados foi {}" .format(conth))
print("A quantidade de mulheres com menos de 20 anos é {}" .format(contm))
 
    