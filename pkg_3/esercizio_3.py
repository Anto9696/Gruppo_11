import os
import hashlib

def find_repetition(dir):
    """Presa la directory dir, restituisce un dizionario contenente le liste dei che sono tra loro file duplicati.
       Se un file non ha duplicati sarà l'unico elemento della lista a cui appartiene. Complessità O(n) con n numero di file"""
    file_tab = {}
    for file in os.listdir(dir):
        try:
            hasher = hashlib.sha256()
            with open(dir+"/"+file,"r") as f:
                buffer = f.read()
                hasher.update(buffer.encode())
                hashing = hasher.hexdigest()
            if hashing not in file_tab:
                file_tab[hashing] = []
            file_tab[hashing].append(file)
        except Exception as e:
            print(e)
    return file_tab