from pkg_2.esercizio2 import Statistics

if __name__ == "__main__":
    stat = Statistics("nomeFile")
    print("FREQUENZA 5", stat[5]._frequency)
    print("TOTALE 5", stat[5]._total)
    print("FREQUENZA", stat[8]._frequency)
    print("TOTALE", stat[8]._total)
    print("LEN", len(stat))
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())
    print("PERCENTILE", stat.percentile())

    print("INSERISCO VALORI")
    for i in range(1,10):
        stat.add(i, i)
        print("key ", i)
        print("FREQUENZA", stat[i]._frequency)
        print("TOTALE", stat[i]._total)

    print("SECONDO FOR")
    for i in range(1,3):
        stat.add(i, i)
        print("key ", i)
        print("FREQUENZA", stat[i]._frequency)
        print("TOTALE", stat[i]._total)

    stat.add(2, 2)
    print("key ", 2)
    print("FREQUENZA", stat[2]._frequency)
    print("TOTALE", stat[2]._total)
    print("LEN", len(stat))
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())

    print("PERCENTILE", stat.percentile())

    print("PIU' FREQUENTI")
    # for i in stat.mostFrequent(5):
    #     print(i)
    mf = stat.mostFrequent(5)
    for i in mf:
        print(i)
