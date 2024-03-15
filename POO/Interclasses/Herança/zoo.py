class Animal:
    def __init__(self) -> None:
        self.classe = "Animal"
        
    def eat(self):
        print(f"{self.__class__.__name__} eating")

    def sleep(self):
        print(f"{self.__class__.__name__} sleeping")

    def walk(self):
        print(f"{self.__class__.__name__} walking")


class Aves(Animal):
    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print(f"Flying")

        
class Penguim(Aves):
    def __init__(self) -> None:
        super().__init__()

    def slip(self):
        print("Sliping")

class Person:
    def __init__(self) -> None:
        pass

    def watch(self, animal: Aves):
        try:
            print("Watching the", end=" ")
            animal.fly()
        except Exception as ex:
            print("\nSomething occured:", ex)

        print("Marmininu")

if __name__ == "__main__":
    roberta = Person()
    tadeu = Penguim()
    fabricio = Animal()

    roberta.watch(tadeu)
    roberta.watch(fabricio)



