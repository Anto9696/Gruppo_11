from pkg_1.esercizio1 import NewAVLTreeMap
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
import os

class Statistics(NewAVLTreeMap):
    class _Element:
        def __init__(self, f, t):
            self._frequency = f
            self._total = t

    def __init__(self, file):
        super().__init__()
        dir = "testing_folder"#input("Inserire una cartella ")
        self._occurrency = 0
        self._sum = 0
        if os.path.isfile(dir+"/"+file+".txt"):
            conn=open(dir+"/"+file+".txt","r")
            data = conn.readlines()
            for d in data:
                [k, v] = d.split(" ")
                self.add(int(k),int(v))

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
        return self._sum / self._occurrency if not self.is_empty() else None

    def median(self):
        """restituisce la mediana delle key presenti nel dataset, definita
        come la key tale che la metà delle occorrenze del dataset hanno key minori o
        uguali della mediana (sugg. tener conto delle frequenze di ciascuna key);"""
        return self.percentile(50)

    def percentile(self, j=20):
        """restituisce il j-imo percentile, per j = 1, … 99, delle
        lunghezze delle key, definito come la key k tale che il j per cento delle
        occorrenze del dataset hanno key minori o uguali di k;"""
        pos = (self._occurrency * j / 100)
        print(pos)
        sum = 0
        for el in self:
            e = self.__getitem__(el)
            sum += e._frequency
            if sum > pos:
                return el

    def mostFrequent(self, j):
        """restituisce la lista delle j key più frequenti"""
        list = HeapPriorityQueue()

        # Complessita O(n*log j)
        for e in self:
            el = self.__getitem__(e)
            if len(list) < j or list.min()[0]<el._frequency:
                if len(list) == j:
                    list.remove_min()
                list.add(el._frequency,e)

        container = [None] * j
        for i in range(j):
            container[j - i - 1] = list.remove_min()[1]

        return container





