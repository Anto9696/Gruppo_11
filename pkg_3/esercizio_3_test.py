from pkg_3.esercizio_3 import find_repetition,find_repetition_2
import os.path

"""copia di versione.txt, versione.txt sono tra loro duplicati"""
"""fake_2 testo_prova.txt testo_prova fake.txt, testo_prova.txt sono tra loro duplicati"""
"""originale non ha duplicati.txt sono tra loro duplicati"""

if __name__=="__main__":
    dir = "testing_folder"#input("Inserire una cartella ")
    if os.path.isdir(dir):
        file_list= find_repetition_2(dir)
        for file in file_list:
            print("Duplicati di "+str(file)+" : "+str(file_list[file]))

        file_list = find_repetition(dir)
        for file in file_list:
            print("Duplicati di " + str(file) + " : " + str(file_list[file]))
    else:
        print("Non è una cartella")
