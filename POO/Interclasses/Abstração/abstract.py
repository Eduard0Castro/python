from abc import ABC, abstractmethod

"""
    Uma classe abstrata não pode ser implementada (instanciada).
    Um método abstrato em uma classe abstrata deve ser implementado na classe herdeira
    Uma classe composta só de métodos abstratos pode ser considerada uma interface em python

"""
class AbstractClass(ABC):

    def __init__(self):
        self.atributo = "Marmininu"

    def method(self, element: str):
        print(element)

    @abstractmethod
    def abstract_method(self):
        print("Fabricio Omuaruma")


class Daughter(AbstractClass):
    def __init__(self):
        super().__init__()

    def present(self):
        print("Hello, Julio")

    def abstract_method(self):
        return super().abstract_method()

if __name__ == "__main__":

    try:
        abstract = AbstractClass()

    except Exception as ex:
        print("Some error occured:", ex)

    daughter = Daughter()
    daughter.abstract_method()




    
    
        
