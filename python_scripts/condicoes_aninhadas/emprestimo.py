casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = float(input('Em quantos anos você pretende pagar o empréstimo? '))

prestacao = (casa/anos)/12

if (prestacao > 0.3*salario):
    print('\n\033[31mVocê não pode financiar essa casa!\033[m')

else:
    print('\n\033[32mPerfeito, vamos prosseguir para os termos do financiamento!\033[m')