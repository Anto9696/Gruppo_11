import os
import hashlib

def find_repetition(dir):
    """Presa la directory dir, restituisce un dizionario contenente le liste dei che sono tra loro file duplicati"""
    file_tab = {}
    for file in os.listdir(dir):
        file_content = open(dir+"/"+file,"r").read()
        hasher = hashlib.md5()
        hasher.update(file_content.encode())
        if hasher.hexdigest() not in file_tab:
            file_tab[hasher.hexdigest()] = []
        file_tab[hasher.hexdigest()].append(file)
    return file_tab