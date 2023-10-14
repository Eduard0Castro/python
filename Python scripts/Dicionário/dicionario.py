filme = {'título': 'O Senhor dos Anéis', 'ano':'2000', 'diretor': 'Peter Jackson'}
lista = [filme]

del(filme['ano'])
filme['produtora'] = 'New Line Cinema'
print(filme['título'])
print(filme.values())
print(filme.keys())
print(filme.items())
print(lista[0]['diretor'])