# Em associação, as classes continuam independentes

class Writer:
    def __init__(self, nome):
        self.__nome = nome
        self.__tool = None

    @property
    def nome(self):
        return self.__nome
    
    @property
    def tool(self):
        return self.__tool
    
    @tool.setter
    def tool(self, tool):
        self.__tool = tool

class Pen:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca
    
    def write(self):
        print("Pen is writting")


class WriterMachine:

    def __init__(self, marca):
        self.marca = marca

    def write(self):
        print("Olivetti is writting")


queiroz = Writer("Queiroz")
pilot = Pen("Pilot")
olivetti82 = WriterMachine("Olivetti")

#Independentes:
print(queiroz.nome)
print(pilot.marca)
pilot.write()
olivetti82.write()

print()

# Associando:
# O atributo __tool da classe Writer recebe o objeto olivetti82 da classe WriterMachine
# tendo acesso a todos os métodos desta última 
queiroz.tool = olivetti82
queiroz.tool.write()
