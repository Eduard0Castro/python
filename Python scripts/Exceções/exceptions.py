
def divide(n1: int, n2: int) -> int:

    if n2 == 0:
        raise ZeroDivisionError("n2 não pode ser zero, vai dar bigode na divisão")

    else:

        return n1/n2


try:
    print(divide(2, 0))

except Exception as zero:
    
    print(zero)

