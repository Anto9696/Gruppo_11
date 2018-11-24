import os
import hashlib

def find_repetition(dir):
    """Presa la directory dir, restituisce un dizionario contenente le liste dei che sono tra loro file duplicati"""
    file_tab = {}
    for file in os.listdir(dir):
        try:
            hasher = hashlib.sha1()
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

def find_repetition_2(dir):
    """Presa la directory dir, restituisce un dizionario contenente le liste dei che sono tra loro file duplicati"""
    file_tab = {}
    for file in os.listdir(dir):
        try:
            with open(dir+"/"+file,"r") as f:
                buffer = f.read()
                hashing = hash(buffer)
            if hashing not in file_tab:
                file_tab[hashing] = []
            file_tab[hashing].append(file)
        except Exception as e:
            print(e)
    return file_tab