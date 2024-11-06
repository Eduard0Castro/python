
class People:
    
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.classname = self.__class__.__name__

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    def speak(self):
        print(f"{self.__nome} está falando")
    

class Client(People):
    def buy(self):
        print(f"{self.nome} está comprando")


class Student(People):
    def study(self):

        if self.classname == "Teacher":
            print(f"{self.nome} já estudou tudo e agora dá aula")

        else:
            print(f"{self.nome} está estudando")
    

# Classe herdando mais de uma classe:
class Teacher(Client, Student):
    def teach(self):
        print(f"{self.nome} is teaching")







if __name__ == "__main__":
    lucio = Student("Lúcio", 18)
    caique = Client("Caique", 18)
    horacio = Teacher("Horácio", 74)
    
    # Métodos comuns da super classe
    lucio.speak()
    caique.speak()
    horacio.speak()

    # Métodos próprios de cada classe herdeira:
    lucio.study()
    caique.buy()

    # Classes que herdam de classes herdadas:
    horacio.buy()
    horacio.study()





    