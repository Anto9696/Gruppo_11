from pkg_1.esercizio2 import Statistics

if __name__ == "__main__":
    stat = Statistics()
    for i in range(1,10):
        stat.add(i, 10 - i)
        print("FREQUENZA", stat[i]._frequency)
        print("TOTALE", stat[i]._total)

    for i in range(1,2):
        stat.add(i, i)
        print("FREQUENZA", stat[i]._frequency)
        print("TOTALE", stat[i]._total)


    print("LEN", len(stat))
    print("MEDIA", stat.average())
    print("OCCORRENZE", stat.occurrences())

    print("PERCENTILE", stat.percentile())

    for i in stat.mostFrequent(3):
        print(i)
