from people import People

p1 = People(43, 21, "M", "Brasileiro", False, True)
p2 = People('Fabrício', 43, 'Masculino', 'Inglês', True, False, "156.423.987-56")
p1.imprimir()
p2.imprimir()

# Testando métodos falar() e comer()
p1.falar()
p2.falar()
p1.comer()
p1.falando = False
p1.comendo = True
p1.comer()
p2.comendo = False
p2.falando = True
p2.falar()

# Imprimindo
print("O ano de nascimento de {} é {}" .format(p1.name, p1.get_year()))
print("O ano de nascimento de {} é {}" .format(p2.name, p2.get_year()))

# Criando objeto por um método de classe
p3 = People.born_year('Eduardo', 2003)
print(p3.get_year())
print(p3.age, p3.name)
p3.imprimir()

# Testando método estático
idp3 = p3.gera_id()
print(idp3)
print(People.gera_id())

# Testando variável de classe:
People.teste = "Alterada"
p1.teste = "Instância de People p1 sobrepondo variável de classe"
print(People.teste)
print(p1.teste) # O interpretador do python procura primeiro na instancia o valor e depois na classe
print(p2.teste)
print(p1.__dict__) # Aqui há 'teste' na instância
print(p2.__dict__) # Aqui só há 'teste' na classe, por isso não aparece

# Método privado(não é possível acessá-lo diretamente):
# print(p2.__present_documentation())

# Maneira de acessá-lo com uma método acessível pela instância
print(p2.olha_as_manha())
print(p1.olha_as_manha())

print(p1)
print(p2)

