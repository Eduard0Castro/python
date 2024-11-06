from pathlib import Path

print(Path(__file__).resolve().parent)
print(Path().absolute())

path_ = "python/Testes"

print(Path(__file__).parent.joinpath(path_))

