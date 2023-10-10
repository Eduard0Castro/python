exp = str(input("Digite uma expressão: "))
pilha = []

for c in exp:
    if c == "(":
        pilha.append("(")

    elif c == ")":
        if len(pilha) > 0:
            pilha.pop()

        else: 
            pilha.append(")")
            break

if len(pilha) == 0 :
    print("\033[32mExpressão válida!\033[31m")
else:
    print("\033[31mExpressão inválida!\033[31m")
