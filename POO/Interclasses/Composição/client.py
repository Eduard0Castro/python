"""
Aqui uma classe evoca a outra, ou seja, há a criação de um objeto da classe Adress
na classe Client. Quando o objeto da classe Client é deletado, os objetos associados da 
classe Adress são deletados também
"""

class Client:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.adresses = list()

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def idade(self):
        return self.__idade

    def insert_adress(self, cidade, estado):
        self.adresses.append(Adress(cidade, estado))

    def list_adresses(self):
        for i, adress in enumerate(self.adresses):
            print("Endereço {} {}" .format(i+1, self.__nome))
            adress.show_adress()

    def __del__(self):
        print(f"Destruindo o objeto {self.__nome}")
            

class Adress:
    def __init__(self, cidade, estado):
        self.city = cidade
        self.state = estado

    def show_adress(self):
        print(f"Cidade: {self.city}\nEstado: {self.state}\n")

    def __del__(self):
        print(f"Destruindo {self.city}/{self.state}")


gustavo = Client("Gustavo", 33)
maria = Client("Maria", 25)
sebastiao = Client("Sebastião", 85)


gustavo.insert_adress("Baependi", "Minas Gerais")
gustavo.insert_adress("Boston", "Massachusetts")
gustavo.insert_adress("Paraibuna", "São Paulo")

maria.insert_adress("Conceição do Rio Verde", "Minas Gerais")

sebastiao.insert_adress("Cruzília", "Minas Gerais")

gustavo.list_adresses()
maria.list_adresses()
sebastiao.list_adresses()

del gustavo

print("\n=======Fim do código=======\n")

