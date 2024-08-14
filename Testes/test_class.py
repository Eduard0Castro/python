
class Test:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address
        self.nada = int()

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self, value: str):
        self._name = value

    @age.setter
    def age(self, value: str):
        self._age = value

    @property
    def nada(self):
        return self._nada
    
    @nada.setter
    def nada(self, value):
        print("Setter")
        self._nada = value
    

test = Test("Eduardo", 21, "Cruzeiro")
print(test.nada)
