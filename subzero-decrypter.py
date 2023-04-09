#!/usr/bin/env python3

import fnmatch
import os
from cryptography.fernet import Fernet

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

try:
    with open("privateKey.key", "rb") as key:
        privKey = key.read()
        
    for dosya in dosyalar:

        with open(dosya, "rb") as dosyaa:
            icerik = dosyaa.read()
    
        sifresiz_icerik = Fernet(privKey).decrypt(icerik)

        with open(dosya, "wb") as dosyaa:
            dosyaa.write(sifresiz_icerik)
except:
    print("[ ! ] Could not read Private Key file.")

try:
    os.remove("privateKey.key")
    print("""
                #########################
                #   SUBZERO DECRYPTED   #
                #########################
    """)
except:
    print("[ ! ] Failed to delete Private Key.")
