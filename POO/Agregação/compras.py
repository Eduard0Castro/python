"""
A agregação faz com que uma classe dependa da outra, como pode-se ver na relação existente entre 
a classe Compras e Product, afinal, alguns métodos de Compras só podem ser executados se houver os 
objetos da classe Product.
"""

class Compras:
    def __init__(self):
        self.products = list()

    def insert_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product.name, product.price)

    def total(self):
        total = 0
        for product in self.products:
            total += product.price
        
        return total
        
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price



desodorante = Product("Desodorante", 18)
sabonete = Product("Sabonete", 2.50)
balm = Product("Balm de barba", 59.90)

compra = Compras()
compra.insert_product(desodorante)
compra.insert_product(sabonete)
compra.insert_product(balm)

compra.list_products()
print("Soma total dos produtos", compra.total())

