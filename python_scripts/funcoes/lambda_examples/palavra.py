palavra = lambda x: True if x[0].upper() =="A" else False
#or
palavra2 = lambda y: y[0].lower() == "a"


print(palavra("Almondega"))
print(palavra("alegria"))
print(palavra("Eduardo"))

print(palavra2("Almondega"))
print(palavra2("alegria"))
print(palavra2("Alermando"))

