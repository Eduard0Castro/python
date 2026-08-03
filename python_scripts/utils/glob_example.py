import glob
from pathlib import Path

print(__file__)
path = Path(__file__).absolute().parent.parent.parent / "files"

print(path)

files = glob.glob(f"{path}/*.txt")
print(files)
