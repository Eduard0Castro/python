from abc import ABC, abstractmethod

"""
Aplicando a ideia de interface na implementação das classes "Product" e "Service".
Isso pode ser útil para fazer com que a classe "Compras" execute seus métodos recebendo
produtos ou serviços que estão padronizados seguindo as normas da interface, o que torna a agregação
mais generalizada e com o poder de embarcar mais tipos de "products".
"""

class IProduct(ABC):

    @abstractmethod
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @abstractmethod
    def __str__(self) -> str:
        printar = f"{self._name}: {self._value}"
        return printar
    

class Product(IProduct):
    def __init__(self, name, value):
        super().__init__(name, value)

    def __str__(self) -> str:
        return super().__str__()
    
class Service(IProduct):
    def __init__(self, name, value):
        super().__init__(name, value)

    def __str__(self):
        return super().__str__()
    

class Compras:
    def __init__(self) -> None:
        self._product = list()

    def insert_product(self, product: IProduct):
        self._product.append(product)

    def list_product(self):
        for product in self._product:
            print(product)

    def total(self) -> float:
        total = 0.0
        for product in self._product:
            total += product._value

        return total


if __name__ == "__main__":
    gorgonzola = Product("Gorgonzola", 17.80)
    balm = Product("Balm de barba", 59.90)
    pintar = Service("Pintar", 200)
    compra = Compras()

    compra.insert_product(gorgonzola)
    compra.insert_product(pintar)
    compra.insert_product(balm)

    compra.list_product()
    print(compra.total())


