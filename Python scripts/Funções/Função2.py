def maluquice():
    #para que num seja utilizada como a mesma 
    #variável em todo o escopo, usa-se 'global' informar ao python
    #que eu quero ele use a variável global já declarada
    global num 
    num = 98
    print(num)

num = 9
print(num)
maluquice()
print(num)


def soma (a = 1, b = 0, c = 0):
    soma = a + b + c
    
    return soma

print(soma (soma(), 5, 6))


def factorial(num):
    fatorial = 1
    for i in range (num, 0, -1):
        fatorial *= i

    return fatorial

print(factorial(5))

def ano():
    #importar módulos dentro das funções economiza memória
    from datetime import date
    ano = date.today().year
    print(ano)




