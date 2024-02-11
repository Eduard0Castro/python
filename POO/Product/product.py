class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percent):
        new_price = self.preco*(1-(percent/100))
        return new_price
    
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, value):
        if isinstance(value, str):
            value = float(value.replace("R$", ""))

        self._preco = value

    # Getter
    @property
    def nome(self):
        return self._nome
    
    # Setter
    @nome.setter
    def nome(self, value):
        self._nome = value.capitalize()

    

p1 = Product('LEITE', 5)
print(p1.nome, p1.desconto(50))
p2 = Product("CANECA", "R$50")
print(p2.nome, p2.desconto(60))

