import shutil 
import os

HOME_PATH = os.path.expanduser("~")
ABSOLUTE_PATH = os.path.abspath("")
SOURCE_FOLDER = f"{ABSOLUTE_PATH}/subdirectory_example/"

if not os.path.exists(SOURCE_FOLDER):
    print("Caminho incorreto. Terminando")
    raise IsADirectoryError("Diretório inexistente")

new_directory = f"{HOME_PATH}/subdirectory_example"

os.makedirs(new_directory, exist_ok=True)

for root, directories,files in os.walk(SOURCE_FOLDER):

    for dir_ in directories:
        os.makedirs(os.path.join(new_directory, os.path.join(root.removeprefix(SOURCE_FOLDER), dir_)), 
                    exist_ok = True)

    for file in files:
        shutil.copy(os.path.join(root, file), os.path.join(new_directory, root.removeprefix(SOURCE_FOLDER)))
