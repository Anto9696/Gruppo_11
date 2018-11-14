from pkg_1.esercizio1 import NewAVLTreeMap


class Statistics(NewAVLTreeMap):
    class _Element:
        def __init__(self, f, t):
            self._frequency = f
            self._total = t

    def __init__(self):
        super().__init__(None)
        self._occurrency = 0

    def add(self, k, v):
        try:
            el = self.__getitem__(k)
            el._frequecy += 1
            el._total += v
            self.__setitem__(k, el)
        except KeyError:
            elem = self.Element(1, v)
            self.__setitem__(k, elem)
        self._occurrency += 1


    def len(self):
        pass

    def occurrences(self):
        pass

    def average(self):
        pass

    def median(self):
        pass

    def percentile(self, j=20):
        pass

    def mostFrequent(self,j):
        pass
