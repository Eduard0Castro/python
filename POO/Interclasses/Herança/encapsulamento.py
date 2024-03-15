"""
Tipos de encapsulamento e onde consegue-se ver cada método:

            Private:    Protected:    Public:
Classe:         X           X           X

Herdeira:                   X           X

Objeto:                     X           X

"""

class Example:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
        self.__using_on_class()

    def __using_on_class(self):
        print(self.public)
        print(self._protected)
        print(self.__private)

class ExampleHerdeira(Example):
    def __init__(self):
        super().__init__()
        self.__using_on_herdeira()


    def __using_on_herdeira(self):
        print(self.public)
        print(self._protected)
        # print(self.__private) ERRO: Private


example = Example()
example_herdeira = ExampleHerdeira()

# example.__using_on_class() ERRO: método private



