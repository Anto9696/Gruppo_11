from pkg_2.esercizio2 import Statistics

if __name__ == "__main__":
    stat = Statistics("testing_folder/nomeFile.txt")
    print("LEN", stat.len())
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())
    print("PERCENTILE", stat.percentile())

    print("INSERISCO VALORI")
    for i in range(1,10):
        stat.add(i, i)

    print("SECONDO FOR")
    for i in range(1,3):
        stat.add(i, i)

    stat.add(2, 2)
    print("key ", 2)
    print("LEN", stat.len())
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())

    print("PERCENTILE", stat.percentile(55))
    print("MEDIANA", stat.median())

    print("PIU' FREQUENTI")

    mf = stat.mostFrequent(3)
    for i in mf:
        print(i)
