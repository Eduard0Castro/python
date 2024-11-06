import threading
from time import sleep

def function_a():
    print("Ola")
    sleep(3)
    print("Sou eu de novo")

def function_b():
    print("Porque")
    sleep(2)
    print("Biruta")

a = threading.Thread(target=function_a)
b = threading.Thread(target=function_b)

a.start()
b.start()






