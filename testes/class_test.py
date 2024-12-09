class TesteAttr:

    LUIS = "Luis"
    def __init__(self) -> None:
        pass

TesteAttr.LUIS = "Kiko"

teste = TesteAttr()
kiko = TesteAttr()

kiko.LUIS = "Kiko"

print(teste.LUIS)
print(kiko.LUIS)
print(TesteAttr.LUIS)