taxa = 0.3

def calcula_preco(preco_liquido: int) -> float:
    preco = preco_liquido + preco_liquido*taxa

    return preco

if __name__ == "__main__":
    print(__name__)
    print(calcula_preco(50))
    
