from pathlib import Path

path = Path().home().resolve()

coordinate_file = path/"coordinates.txt"
final = list()

with open(coordinate_file, "r") as file:
    coordinates = file.readlines()
    
    for coordinate in coordinates:
        components = coordinate.split(",")
        inter = [float(element) for element in components]
        final.append(tuple(inter))

        
        
lista = [print(lat, long, alt) for lat, long, alt in final]
print(lista)
