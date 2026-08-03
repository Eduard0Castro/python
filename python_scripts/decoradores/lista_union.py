from itertools import zip_longest


def list_zipper(list_one: list, list_two: list)-> list:
    size = min(len(list_one), len(list_two))
    return [(list_one[i], list_two[i]) for i in range(size)]


one = ["Salvador", "Ubatuba", "Belo Horizonte"]
two = ["BA", "SP", "MG", "RJ"]

print(list_zipper(one, two))
print(list(zip(one, two)))
print(list(zip_longest(one, two, fillvalue="No City")))