
def multi():
    return 9*3

def div():
    return 9/3

functions = {0: multi, 
             10: div}


func = functions.get(int(input("Digita ai: ")), None)
if func: print(func())


galgo = [1, "list", div, 1.32]

mallinois = galgo[:]
mallinois.reverse()

print(mallinois)
print(galgo)