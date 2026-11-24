import os
from cryptography.fernet import Fernet
from pathlib import Path

data_dir = Path(__file__).resolve().parent.parent / "testovaci_data"

files = []

key = Fernet.generate_key()

with open("Key.key", "rb") as Key:
    secret = Key.read()

for file in data_dir.iterdir():
    if file.is_file() and not file.is_symlink():
        files.append(file)

for file in files:
    with open(file, "rb") as File:
        contents = File.read()
    contents_decrypted = Fernet(secret).decrypt(contents)
    with open(file, "wb") as File:
        File.write(contents_decrypted)