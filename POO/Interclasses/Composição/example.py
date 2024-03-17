"""
Instanciar um objeto de uma classe dentro de outra é a relação denominada composição
e tem a capacidade de evitar a herança, afinal proporciona que a classe que instancia um objeto 
de uma outra em sua implementação tenha acesso aos métodos desta outra sem herdá-la diretamente
"""

class Insert:

    def __init__(self) ->None:
        self.regis = list()

    def insert_one(self, element):
        self.regis.append(element)
        return self.regis
    
    def insert_many(self, elements: tuple)-> list:
        for element in elements:
            self.regis.append(element)
        return self.regis
    

class Select:

    def select_one(self, index: int, lista: list):
        return lista[index]
    
    def select_many(self, indexes: tuple, lista: list):
        selected = list()
        for index in indexes:
            selected.append(lista[index])

        return selected
            

class Project:

    def __init__(self, name: str) ->None:
        self._name = name
        self._members = list()

        self._insert = Insert()
        self._select = Select()

    def insert_member(self, name, n_registration):
        self._members = self._insert.insert_one((name, n_registration))

    def more_than_one(self, *members):
        self._members = self._insert.insert_many(members)

    def members(self):
        return self._members
    
    def search(self, *indexes: int) -> list:
    
        if len(indexes) == 1:
            return self._select.select_one(indexes[0], self._members)
        
        elif len(indexes) > 1:
            return self._select.select_many(indexes, self._members)
        
    @classmethod
    def create_object(cls, name: str):
        new_obj = cls(name)
        return new_obj
        


bleble = Project("Ble ble")

bleble.insert_member("Low", 2021009360)
bleble.insert_member("Kiko", 2023005420)
bleble.insert_member("Maiara", 2019684587)
bleble.more_than_one(("Julio", 2024879654), ("Sem Dedo", 2023001456))

print(bleble.members())
print(bleble.search(4, 1))