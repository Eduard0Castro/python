times = ('Flamengo', 'Palmeiras', 'Botafogo', 'Bragantino', 'Fluminense', 
         'Grêmio', 'Internacional', 'Sampaio Corrêa', 'Asa de Arapiraca', 'Bicas')

print(f"\nOs quatro primeiros da tupla: \033[32m{times[0:4]}\033[m")
print(f"\nOs três últimos colocados: \033[31m{times[7:10]}\033[m")
print("Lista em ordem alfabética: {}" .format(sorted(times)))
print("Onde está o Sampaio Corrêa na tupla? {}ª posição\n" .format(times.index('Sampaio Corrêa')+1))