from datetime import datetime
from random import randint

class People:
    data = datetime.today()
    year = data.year
    teste = 43

    def __init__(self, nome, idade, genre, nacionalidade, comendo = False, falando = False):
        self.name = nome
        self.age = idade
        self.genre = genre
        self.nacionality = nacionalidade
        self.comendo = comendo
        self.falando = falando


    def imprimir(self):
        print("Nome: {}\nIdade: {}\nGênero: {}\nNacionalidade: {}" 
              .format(self.name, self.age, self.genre, self.nacionality))
        print()
        
    def falar(self):
        if self.comendo == True:
            print(f"{self.name} não pode falar comendo")

        elif self.falando == True:
            print("{} está falando" .format(self.name))

        else:
            print("Ninguém está falando")
        
    def comer(self, alimento = 'algum alimento'):
        if self.falando == True:
            print(f"{self.name} não pode comer falando")

        elif self.comendo == True:
            print(f"{self.name} está comendo {alimento}")

        else:
            print("Ninguém está comendo")
    
    def get_year(self):
        year = self.year - self.age
        return year

    #Método de classe que fabrica um objeto dessa classe que relaciona
    #a classe e não a instância
    @classmethod
    def born_year(cls, name, year):
        idade = cls.year - year
        return cls(name, idade, "Masculino", "Brasileiro")
    
    # Método estático não utiliza nem a classe nem a instância
    # Como se fosse uma função normal que está dentro da classe por organização
    # Pode ser utilizado tanto pela instancia quanto pela classe em si
    @staticmethod
    def gera_id():
        id = randint(0, 100)
        return id


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):

        if not isinstance(value, str):
            value = str(value)
        print("Estou aqui")
        self._name = value.capitalize()
    

        