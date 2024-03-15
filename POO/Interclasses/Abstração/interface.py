from abc import ABC, abstractmethod
from math import pow

"""
A interface fornece métodos padrões que são, obrigatoriamente, implementadas por cada herdeira, cada qual com
sua especificidade.
Ou seja, como no caso do engenheiro, ele mede um elemento que tem um formato padrão 
(formato da interface) e consegue-se obter o perimetro e area de qualquer terreno com o 
formato seguindo o padrão designado pela classe abstrata
"""

class IFormats(ABC):
 
    @abstractmethod
    def perimeter(self)->int:
        pass

    @abstractmethod
    def area(self)->int:
        pass


class Square(IFormats):
    def __init__(self, side) -> None:
        self.side = side

    def perimeter(self):
        return 4*self.side
    
    def area(self):
        return pow(self.side, 2)
    

class Rectangle(IFormats):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def perimeter(self):
        return 2*(self.width + self.height)
    
    def area(self):
        return self.width*self.height
    

class Engineer:
    def __init__(self, name) -> None:
        self.name = name

    def measure_perimeter(self, terreno: IFormats):
        perimeter = terreno.perimeter()
        print(f"{self.name} measured {perimeter}m")

    def measure_area(self, terreno: IFormats):
        area = terreno.area()
        print(f"{self.name} measured {area}m2")



if __name__ == "__main__":
    square = Square(5)
    rectangle = Rectangle(5, 3)
    eduardo = Engineer("Eduardo")

    eduardo.measure_perimeter(square)




