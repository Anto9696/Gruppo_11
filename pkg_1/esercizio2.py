from pkg_1.esercizio1 import NewAVLTreeMap
from TdP_collections.priority_queue.sorted_priority_queue import SortedPriorityQueue


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
        """aggiunge la coppia (k, v) alla mappa; se la chiave k è già presente
        nella mappa deve aggiornare i campi frequency e total"""
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
        """restituisce il numero di chiavi presenti nella mappa;"""
        return super().__len__()

    def occurrences(self):
        """restituisce la somma delle frequenze di tutti gli elementi
        presenti nella mappa"""
        return self._occurrency

    def average(self):
        """estituisce la media dei valori di tutte le occorrenze presenti nel
        dataset"""
        return self._sum / self._occurrency

    def median(self):
        """restituisce la mediana delle key presenti nel dataset, definita
        come la key tale che la metà delle occorrenze del dataset hanno key minori o
        uguali della mediana (sugg. tener conto delle frequenze di ciascuna key);"""
        return self.percentile(50)

    def percentile(self, j=20):
        """restituisce il j-imo percentile, per j = 1, … 99, delle
        lunghezze delle key, definito come la key k tale che il j per cento delle
        occorrenze del dataset hanno key minori o uguali di k;"""
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
        """restituisce la lista delle j key più frequenti"""
        list = SortedPriorityQueue()
        for e in self:
            el = self.__getitem__(e)
            list.add(el._frequency,e)
        for i in range(self.len()-j):
            list.remove_min()

        for i in range(j):
            yield list.remove_min()[0]



if __name__ == "__main__":
    cacca = Statistics()
    for i in range(1,10):
        cacca.add(i,10-i)
        print("FREQUENZA",cacca[i]._frequency)
        print("TOTALE",cacca[i]._total)

    for i in range(1,2):
        cacca.add(i,i)
        print("FREQUENZA",cacca[i]._frequency)
        print("TOTALE",cacca[i]._total)


    print("LEN",len(cacca))
    print("MEDIA",cacca.average())
    print("OCCORRENZE",cacca.occurrences())

    print("PERCENTILE",cacca.percentile())

    for i in cacca.mostFrequent(3):
        print(i)

