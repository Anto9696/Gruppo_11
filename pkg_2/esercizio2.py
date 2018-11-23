from pkg_1.esercizio1 import NewAVLTreeMap
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
import os


class Statistics:
    class _Element:
        def __init__(self, f, t):
            self._frequency = f
            self._total = t

    def __init__(self, file):
        self._newAVLTreeMap = NewAVLTreeMap()
        self._occurrency = 0
        self._sum = 0
        if os.path.isfile(file):
            conn = open(file, "r")
            data = conn.readlines()
            for d in data:
                [k, v] = d.split(" ")
                self.add(int(k), int(v))

    def add(self, k, v):
        """aggiunge la coppia (k, v) alla mappa; se la chiave k è già presente
        nella mappa deve aggiornare i campi frequency e total"""
        try:
            el = self._newAVLTreeMap[k]
            el._frequency += 1
            el._total += v
            self._newAVLTreeMap[k] = el
        except KeyError:
            elem = self._Element(1, v)
            self._newAVLTreeMap[k]= elem
        self._sum += v
        self._occurrency += 1

    def len(self):
        """restituisce il numero di chiavi presenti nella mappa;"""
        return len(self._newAVLTreeMap)

    def occurrences(self):
        """restituisce la somma delle frequenze di tutti gli elementi
        presenti nella mappa"""
        return self._occurrency

    def average(self):
        """estituisce la media dei valori di tutte le occorrenze presenti nel
        dataset"""
        if not self._newAVLTreeMap.is_empty():
            return self._sum / self._occurrency
        else:
            raise ValueError("The object is empty")

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
        sum = 0
        for e in self._newAVLTreeMap.items():
            sum += e[1]._frequency
            if sum > pos:
                return e[0]

    def mostFrequent(self, j):
        """restituisce la lista delle j key più frequenti"""
        list = HeapPriorityQueue()

        for e in self._newAVLTreeMap.items():
            if len(list) < j or list.min()[0] < e[1]._frequency:
                if len(list) == j:
                    list.remove_min()
                list.add(e[1]._frequency, e[0])

        container = [None] * j
        for i in range(j):
            container[j - i - 1] = list.remove_min()[1]

        return container
