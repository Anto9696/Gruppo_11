from pkg_3.esercizio_3 import find_repetition
import os.path

"""copia di versione.txt, versione.txt sono tra loro duplicati"""
"""fake_2 testo_prova.txt, testo_prova fake.txt, testo_prova.txt sono tra loro duplicati"""
"""originale non ha duplicati.txt"""

if __name__=="__main__":
    dir = input("Inserire una cartella ")
    if os.path.isdir(dir):
        file_list = find_repetition(dir)
        for file in file_list.values():
            if len(file) > 1:
                print("Sono duplicati fra loro "+str(file))
            else:
                print(str(file[0])+ " non ha duplicati")
    else:
        print("Non è una cartella")
