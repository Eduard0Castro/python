operacao = [float(input("Digite o primeiro numero: ")), 
 float(input("Digite o segundo numero: ")), 
 str(input("Digite o sinal da operação desejada: "))]
value = operacao[0]

oper = {"+": value.__add__, 
        "-": value.__sub__, 
        "*": value.__mul__, 
        "/": value.__truediv__}

def calculator(args: list) -> float:
    return oper.get(args[2], None)(args[1])
    

print(calculator(operacao))



