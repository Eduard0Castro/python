class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, comp):
        r = self.real + comp.real
        i = self.img + comp.img
        return Complex(r, i)
    
    def __add__(self, comp):
        r = self.real + comp.real
        i = self.img + comp.img
        return Complex(r, i)
    
    def sub(self, comp):
        r = self.real - comp.real
        i = self.img - comp.img
        return Complex(r, i)
    
    def __sub__(self, comp):
        r = self.real - comp.real
        i = self.img - comp.img
        return Complex(r, i)
    
    def imprimir(self):
        if self.img < 0:
            print(f"{self.real} {self.img}i")

        else:
            print(f"{self.real} +{self.img}i")


comp1 = Complex(5, 9)
comp2 = Complex(2, 13)
comp3 = comp1 - comp2
comp4 = comp1 + comp2

comp1.imprimir()
comp2.imprimir()
comp3.imprimir()
comp4.imprimir()

