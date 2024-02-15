class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, comp):
        r = self.real + comp.real
        i = self.img + comp.img
        return Complex(r, i)
    
    def __add__(self, comp):
        return self.add(comp)
    
    def sub(self, comp):
        r = self.real - comp.real
        i = self.img - comp.img
        return Complex(r, i)
    
    def __sub__(self, comp):
        return self.sub(comp)

    def __str__(self):
        if self.img < 0:
            printar = f"{self.real} {self.img}i"

        else:
            printar = f"{self.real} +{self.img}i"

        return printar


comp1 = Complex(5, 9)
comp2 = Complex(2, 13)
comp3 = comp1 - comp2
comp4 = comp1 + comp2

print(comp1)
print(comp2)
print(comp3)
print(comp4)

