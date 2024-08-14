
"""
    args faz com que os argumentos não nomeados passados para a função sejam acoplados em uma 
    tupla. Já kwargs são os argumentos nomeados passados a função que são acoplados em um 
    dicionário. 
"""
def kwargs_example(*args, **kwargs):
    print(args)
    print(kwargs)
    print()
    print(kwargs.get("tupla", ("Nao tem", 0)))

    try:
        print(kwargs["outras"])

    except Exception as ex:
        print("Exceção")
        print(ex)

    else:
        print("Não deu problema")

    finally:
        print("Finalizei aqui, beleza!?")

kwargs_example("Teste args", nomeado = "Teste kwargs", tupla = 'Mais teste kwargs', outra = ("Fuboga", 43))

print()
example_dict = {1: ("Teste um", 0X11111111), "VALUE": ("FUBANGO")}
print(example_dict.get("VALUE", ("O tal do python é muito foda", 10)))
