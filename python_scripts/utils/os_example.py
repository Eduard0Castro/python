import os
import subprocess #cause os.systems is deprecated
from time import sleep
from pathlib import Path
from itertools import count
import math

print("Testanto subprocess") # Isso será apagado no terminal

sleep(1.0)

response = subprocess.run("clear") # os.system is deprecated
response.check_returncode()

print("Terminal limpo")
print("Testando comando run do subprocess com 'pwd' command: ")
subprocess.run("pwd")
print()


file_path = os.path.abspath(".")
print("Testando os.path.abspath: ")
print(file_path)
print()


print("Testando o listdir:")
print(os.listdir())
print()

path = Path().absolute().resolve().parent.parent
print(path)
print()


print("DIRETÓRIOS DESDE A PASTA PYTHON:")


counter = count()


def size_format(file_size: int, base: int = 1000) -> str:

    if file_size <= 0: return "OB"

    units: list = ["B", "KB", "MB", "GB", "TB"]
    index = int(math.log(file_size, base,))

    power = base ** index
    size = file_size/power

    return f"{size:.2f}{units[index]}"


for (root, directory, files) in os.walk(path):
    the_counter = next(counter)
    
    # print(the_counter, root)
    # print("    ", directory)
    for file in files:
        print(f"File name: {file} ->", size_format(file_size = os.path.getsize(os.path.join(root, file))))

# for directory in os.walk(path):
#     for folder in directory[1]:
#         lista2.append(folder)
#         print(folder)

