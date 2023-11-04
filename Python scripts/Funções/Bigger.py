from time import sleep
def bigger(*num):
    size = len(num)
    maior = num[0]
    print("Foram colocados {} elementos" .format(size))
    print("Entre:", end = ' ')
    for i in range(0, size):
        print (num[i], end=' ', flush = True)
        sleep(0.5)
        if(maior < num[i]):
            maior = num[i]
    print("\nO maior é: {}" .format(maior))


bigger(58, 27, 45, 96, 84, 15, 90)
bigger(988, 455, 565, 784, 102, 12, 9874, 10587)






