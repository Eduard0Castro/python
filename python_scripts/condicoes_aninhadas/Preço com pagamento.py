from unidecode import unidecode
valor = int(input('Qual o valor normal do produto que você quer comprar? R$'))
pag = unidecode(str(input('Qual é o método de pagamento? Você tem as seguintes opções: \n-À vista: dinheiro ou cheque \n-À vista no cartão \n-Até duas vezes no cartão \n-Três vezes ou mais no cartão: \n--')).lower())

if pag == 'a vista':
    pag_2 = unidecode(str(input('Dinheiro, cheque ou cartão? ').lower()))
    if pag_2 == 'dinheiro' or pag_2 == 'cheque':
        print(f'O valor do produto é {valor*0.9}')
    elif pag_2 == 'cartao':
        print(f'O valor do produto é {valor*0.95}')
    else:
        print('\033[31mDigita direito, filhão!!!')
elif pag == 'duas vezes no cartao':
    print('O preço é de {}' .format(valor*1))
elif pag == 'tres vezes ou mais no cartao':
    print('O valor é de {}' .format(1.2*valor))
else:
    print('\033[31mDIGITA DIREITO!!!\033[m')

