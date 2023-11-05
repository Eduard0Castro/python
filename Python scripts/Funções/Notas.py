def nota(*notas, sit = False):

    """
    notas => quantas notas forem necessárias. Passe os valores!

    sit => True or False. Indica se quer ver a situação geral das notas.

    This function returns one dictionary with the quantity, highest and lowest score,
    average and the situation if you need.

    """
    maior = notas[0]
    menor = notas[0]
    soma = 0
    dic = dict()
    for i in range(0, len(notas)):
        if maior < notas[i]:
            maior = notas[i]
        if menor > notas[i]:
            menor = notas[i]

        soma += notas[i]

    media = soma/len(notas)
    dic['quantidade'] = len(notas)
    dic['maior'] = maior
    dic['menor'] = menor
    dic ['media'] = media

    if sit == True:
        if media < 7 and media > 5:
            dic['situação'] = "Razoável"
        elif media > 7:
            dic['situação'] = "Boa"
        else:
            dic['situação'] = "Ruim"

    return dic

print(nota(2,7,8,9,5,10, sit=True))


    

        