from pkg_2.esercizio2 import Statistics

if __name__ == "__main__":
    stat = Statistics("nomeFile")
    # print("LEN", len(stat))
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())
    print("PERCENTILE", stat.percentile())

    # print("INSERISCO VALORI")
    # for i in range(1,10):
    #     stat.add(i, i)
    #     # print("key ", i)
    #     # print("FREQUENZA", stat[i]._frequency)
    #     # print("TOTALE", stat[i]._total)
    #
    # print("SECONDO FOR")
    # for i in range(1,3):
    #     stat.add(i, i)
    #     # print("key ", i)
    #     # print("FREQUENZA", stat[i]._frequency)
    #     # print("TOTALE", stat[i]._total)
    #
    # stat.add(2, 2)
    # print("key ", 2)
    # print("FREQUENZA", stat[1]._frequency)
    # print("TOTALE", stat[1]._total)
    print("LEN", stat.len())
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())

    print("PERCENTILE", stat.percentile(55))
    print("MEDIANA", stat.median())

    print("PIU' FREQUENTI")
    # for i in stat.mostFrequent(5):
    #     print(i)
    mf = stat.mostFrequent(2)
    for i in mf:
        print(i)
