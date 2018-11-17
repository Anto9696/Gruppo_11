from pkg_3.esercizio_3 import find_repetition
import os.path


if __name__=="__main__":
    dir = "testing_folder"#input("Inserire una cartella ")
    if os.path.isdir(dir):
        file_list = find_repetition(dir)
        for bucket in file_list.keys():
            print(file_list[bucket])
    else:
        print("Non è una cartella")
