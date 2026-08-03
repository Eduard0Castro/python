# Decorators com paramêtros:
def decorator_factory(param1, param2):

    """
    Essa função permite passar decoradores com parâmetros, de modo que o meu decorador, bem como 
    a função wrapper interna tenha acesso a esses parâmetros.
    """

    def decorar(func) -> callable:
        print(param1)
        print(param2)

        def wrapper(*args, **kwargs):

            print("Decorando")

            result = func(*args, *kwargs)

            return result
        
        return wrapper
        
    return decorar
    

#Posso passar mais de um decorador:
# A ordem em que são executados
@decorator_factory("Segundo", "Decorador")
@decorator_factory("Aloe Vera", "Thorzinho")
def test(x, y) -> None:

    print(test.__name__) # Python troca essa função pela função interna do meu decorator.

    return x + y


print(test(9, 6))



