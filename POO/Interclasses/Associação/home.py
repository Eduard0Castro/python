
class Person:
    def __init__(self, name)->None:
        self.home = None
        self.name = name

    def set_home(self, home):
        self.home = home

    def show_local(self):
        return self.home.adress
    
    def present_yourself(self):
        print(f"Hello, I'm the owner {self.name}.")
    


class Home:
    def __init__(self) -> None:
        self.__adress = "Avenida BPS"
        self.owner = None

    def set_owner(self, owner: Person):
        self.owner = owner

    def get_owner(self):
        return self.owner

    @property
    def adress(self):
        return self.__adress
    
    @adress.setter
    def set_adress(self, new):
        self.__adress = new



lino = Home()
gui = Person("Gui")

# Mudando endereço pelo set_adress
print(lino.adress)
lino.set_adress = "Rua Romão Carneiro"
print(lino.adress)

# Testando a associação 1:
lino.set_adress = "Rua Joaquim Antônio Dias de Castro"
gui.set_home(lino)
print(gui.show_local())

#Testando a associação 2:
lino.set_owner(gui)
owner = lino.get_owner()
owner.present_yourself()





    

