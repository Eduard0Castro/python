class Store:
    tarifa = 1.03

    def __init__(self, adress: str) -> None:
        self.__adress = adress

    def show_adress(self) -> None:
        print(self.__adress)

    @classmethod
    def sell(cls) -> int:
        return 43*cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, new):
        cls.tarifa = new

benja = Store("Benja nazista")
back = Store("Judeu")

print(back.sell())
print(benja.sell())

benja.alterar_tarifa(1.5)

print(back.sell())
print(benja.sell())
print(back.tarifa)


