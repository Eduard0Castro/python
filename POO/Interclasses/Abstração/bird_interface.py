from abc import ABC, abstractmethod

"""
Notar que penguim não tem uma implementação do método fly propriamente dita.

Princípio da Segregação de Interface:
Isso para exemplificar que as classes que herdam a interface podem não implementar um determinado
método que são obrigadas a implementar. Isso justifica a utilização de interfaces mais específicas,
como por exemplo "IFlyingBird" que seria só para as aves que voam, não abrangendo a classe Penguim:

Princípio da segregação de interface:
Ter uma classe padrão (interface) para ditar a criação de classes que serão utilizadas em associações
com outras classes e possibilitar a troca rápida de um tipo seguindo os modelos da interface por ou
tro também nos mesmos moldes sem maiores problemas.
"""

class IBird(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
        self.class_name = self.__class__.__name__

    @abstractmethod
    def eat(self):
        raise "Should be implemented eat method"
    
    @abstractmethod
    def sleep(self):
        raise "Should be implemented sleep method"
    
    @abstractmethod
    def fly(self):
        raise "Should be implemented fly method"
    
    @abstractmethod
    def scream(self):
        raise "Should be implemented scream method"
    

class Halk(IBird):
    def __init__(self) -> None:
        super().__init__()

    def eat(self):
        print(f"{self.class_name} is eating")
        
    def sleep(self):
        print(f"{self.class_name} is sleeping")

    def fly(self):
        print(f"{self.class_name} is flying")

    def scream(self):
        print(f"{self.class_name} is screaming")


class Penguim(IBird):

    def __init__(self) -> None:
        super().__init__()
        
    def eat(self):
        print(f"{self.class_name} is eating")
        
    def sleep(self):
        print(f"{self.class_name} is sleeping")

    def fly(self):
        None

    def scream(self):
        print(f"{self.class_name} is screaming")

    def __mate(self):
        print(f"{self.class_name} is mating")


class Observer:
    def __init__(self, bird: IBird):
        self.__bird = bird

    def see_eat(self):
        self.__bird.eat()
    
    def see_sleeping(self):
        self.__bird.sleep()

    def see_flying(self):
        self.__bird.fly()

    def see_screaming(self):
        self.__bird.scream()

    


if __name__ == "__main__":

    gui = Penguim()
    tadeu = Halk()
    luis = Observer(tadeu)
    
    gui.eat()
    tadeu.fly()
    luis.see_screaming()
    
