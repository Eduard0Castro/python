def factorial(num, show = False):
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i
        if show:
            if i == 1:
                print(i, "=", end=' ')
                break
            print(i, "X", end=' ')
    return fatorial

print(factorial(5, True))
