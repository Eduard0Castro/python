
class Political:

    def __init__(self, nome = "", cargo = "", partido = ""):
        self.nome = nome
        self.cargo = cargo
        self.partido = partido

    def read(self):
        self.nome = str(input("Digite o nome do político: "))
        self.cargo = str(input("Digite o cargo desse político: "))
        self.partido = str(input("Digite o partido do político: "))

    def __str__(self):
        return f"\nNome: {self.nome}\nCargo: {self.cargo}\nPartido: {self.partido}"
    
    def __del__(self):
        print("Destruindo political")
    

class President(Political):
    
    def __init__(self, nome = "", cargo = "", partido = "", country = ""):
        super().__init__(nome, cargo, partido)
        self.country = country

    def read(self):
        super().read()
        self.country = str(input("Digite o país do político: "))

    def __str__(self):
        politico = super().__str__()
        presidente = f"\nPaís: {self.country}"
        return politico + presidente


class Governor(President):

    def __init__(self, nome = "", cargo = "", partido = "", country = "", state = ""):
        President.__init__(self, nome, cargo, partido, country)
        self.state = state

    def read(self):
        President.read(self)
        self.state = str(input("Digite o estato do politico: "))

    def __str__(self):
        return super().__str__() + f"\nEstado: {self.state}"
    

class Mayor(Governor):

    def __init__(self, nome = "", cargo = "", partido = "", country = "", state = "", city = ""):
        super().__init__(nome, cargo, partido, country, state)
        self.city = city

    def read(self):
        super().read()
        self.city = str(input("Digite o nome da cidade: "))

    def __str__(self):
        return super().__str__() + f"\nCidade: {self.city}"
    
class Councilor(Mayor):

    def __init__(self, nome = "", cargo = "", partido = "", country = "", 
                       state = "", city = "", neighborhood = ""):
        
        super().__init__(nome, cargo, partido, country, state, city)
        self.neighborhood = neighborhood

    def read(self):
        super().read()
        self.neighborhood = str(input("Digite o nome do bairro do político: "))

    def __str__(self):
        return super().__str__() + f"\nBairro: {self.neighborhood}"

    

if __name__ == "__main__":
    
    trump = President("Trump", "President", "Republican", "USA")
    maluf = Mayor("Paulo Maluf", "Mayor", "PMDB", "Brazil", "São Paulo", "São Paulo")

    print(trump)
    print(maluf)
    print()
    

