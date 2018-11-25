from pkg_2.esercizio2 import Statistics

if __name__ == "__main__":
    stat = Statistics("testing_folder/nomeFile.txt")
    print("LEN", stat.len())
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())
    print("PERCENTILE", stat.percentile(10))
    print("MEDIANA", stat.median())
    print("PIU' FREQUENTI")

    mf = stat.mostFrequent(3)
    for i in mf:
        print(i)
