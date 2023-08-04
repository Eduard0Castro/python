from random import choice
poss = ['pedra', 'papel', 'tesoura']

while True:
    escolha = str(choice(poss))
    usu = str(input('\033[35mJOKENPO:\033[m ')).lower()


    if (escolha == 'pedra' and usu == 'tesoura') or (escolha == 'tesoura' and usu == 'papel') or (escolha == 'papel' and usu == 'pedra'):
        cap = escolha.capitalize()
        usu = usu.capitalize()
        print('\033[31mO computador venceu! {} X {}\033[m' .format(cap, usu))
    elif escolha == usu:
        print('Iguais, joguemos de novo!')
    else:
        cap = escolha.capitalize()
        usu = usu.capitalize()
        print('\033[32mVocê venceu, meus parabéns!!!{} X {}\033[m' .format(cap, usu))

