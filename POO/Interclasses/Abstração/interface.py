from abc import ABC, abstractmethod
from math import pow

"""
A interface fornece métodos padrões que são, obrigatoriamente, implementadas por cada herdeira, 
cada qual com sua especificidade.
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
    
class UndefinedShapes(IFormats):
    def __init__(self, side) -> None:
        self.side = side

    def perimeter(self):
        return self.side**3
    
    def area(self):
        return 1/3*self.side**2
        
    
class TesteFormats(UndefinedShapes, Square):
    def __init__(self, side) -> None:
        super().__init__(side)

    
class Engineer:
    def __init__(self, name) -> None:
        self.name = name

    def measure_perimeter(self, terreno: IFormats):
        perimeter = terreno.perimeter()
        print(f"{self.name} measured {perimeter}m")

    def measure_area(self, terreno: IFormats):
        area = terreno.area()
        print(f"{self.name} measured {area:.2f}m2")



if __name__ == "__main__":
    square = Square(5)
    rectangle = Rectangle(5, 3)
    eduardo = Engineer("Eduardo")

    luis_format = UndefinedShapes(15)
    formato = TesteFormats(8)
    print(formato.perimeter())

    eduardo.measure_perimeter(square)
    eduardo.measure_area(formato)




