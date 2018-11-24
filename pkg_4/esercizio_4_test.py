from pkg_4.esercizio_4 import circular_substring

if __name__ == "__main__":    #FARE RUN PER ESEGUIRE IL TEST
    decision = "y"
    while(decision == "y"):
        T = input("Inserisci il testo T: ")
        P = input("Inserisci il pattern da cercare per il quale vuoi sapere se è una sottostringa circolare di T: ")
        try:
            result = circular_substring(P, T)
            if result!=-1:
                print("P è una sottostringa circolare di T")
            else:
                print("P non è una sottostringa circolare di T")
        except ValueError:
            print("Hai inserito una stringa vuota!")

        decision = input("Vuoi eseguire un altro test? [Y/N]").lower()