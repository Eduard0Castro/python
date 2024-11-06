import time

sei_la = (input('Digite algo: '))

print('É numérico?: {}' .format(sei_la.isnumeric())) #é possível converter o que foi digitado 
                          #para numerico? Ou seja, int?
print(sei_la.isalpha())

print(sei_la.isalnum())
print(sei_la.isprintable())