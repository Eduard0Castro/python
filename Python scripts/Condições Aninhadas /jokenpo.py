from random import choice
from time import sleep
poss = ['pedra', 'papel', 'tesoura']

while True:
    escolha = str(choice(poss))
    usu = str(input('\033[1;35mPedra, Papel ou Tesoura??:\033[m ')).lower()

    print('\033[1;34mJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO\033[m\n')
    print('-='*20)
    print(f'Computador jogou {escolha.capitalize()}, jogador jogou {usu.capitalize()}')
    if (escolha == 'pedra' and usu == 'tesoura') or (escolha == 'tesoura' and usu == 'papel') or (escolha == 'papel' and usu == 'pedra'):
        cap = escolha.capitalize()
        usu = usu.capitalize()
        print('\033[31mO computador venceu!\033[m')
    elif escolha == usu:
        print('Iguais, joguemos de novo!')
    elif usu == 'pedra' or usu == 'tesoura' or usu == 'papel':
        cap = escolha.capitalize()
        usu = usu.capitalize()
        print('\033[32mVocê venceu, meus parabéns!!!\033[m')
    else:
        print('\033[1;31mDIGITA DIREITO OU NÃO JOGA!\033[m')
    print('-='*20, '\n')

