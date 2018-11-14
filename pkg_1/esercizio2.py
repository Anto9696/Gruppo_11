from pkg_1.esercizio1 import NewAVLTreeMap


class Statistics(NewAVLTreeMap):
    class _Element:
        def __init__(self, f, t):
            self._frequency = f
            self._total = t

    def __init__(self):
        super().__init__()
        self._occurrency = 0
        self._sum = 0

    def add(self, k, v):
        try:
            el = self.__getitem__(k)
            el._frequency += 1
            el._total += v
            self.__setitem__(k, el)
        except KeyError:
            elem = self._Element(1, v)
            self.__setitem__(k, elem)
        self._sum += v
        self._occurrency += 1

    def len(self):
        return super().__len__()

    def occurrences(self):
        return self._occurrency

    def average(self):
        return self._sum / self._occurrency

    def median(self):
        return self.percentile(50)

    def percentile(self, j=20):
        pos = round(self._occurrency * j / 100)
        # print("AAA",pos)
        sum = 0
        for el in self:
            e = self.__getitem__(el)
            # print(el,"AAAAAAAA", sum)
            sum += e._frequency
            if sum > pos:
                return el

    def mostFrequent(self, j):
        pass


if __name__ == "__main__":
    cacca = Statistics()
    # cacca.add(4, 4)
    # cacca.add(4, 4)
    # cacca.add(4, 4)
    # print("FREQUENZA",cacca[4]._frequency)
    # print("TOTALE",cacca[4]._total)
    # cacca.add(1, 5)
    # cacca.add(1, 6)
    # cacca.add(1, 6)
    for i in range(1,10):
        cacca.add(i,10-i)
        print("FREQUENZA",cacca[i]._frequency)
        print("TOTALE",cacca[i]._total)

    for i in range(1,2):
        cacca.add(i,i)
        print("FREQUENZA",cacca[i]._frequency)
        print("TOTALE",cacca[i]._total)

    # print("FREQUENZA",cacca[1]._frequency)
    # print("TOTALE",cacca[1]._total)

    print("LEN",len(cacca))
    print("MEDIA",cacca.average())
    print("OCCORRENZE",cacca.occurrences())

    print("PERCENTILE",cacca.percentile())
