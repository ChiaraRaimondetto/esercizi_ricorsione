from functools import lru_cache
from time import time


class Fibonacci:
    def __init__(self):
        self.cache= {0:0,1:1}
        self.ricorsioni=0
        self.ricorsioni_cache=0

    @lru_cache
    def calcola_elemento_lru(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento_lru(n - 1) + self.calcola_elemento_lru(n - 2)

    def calcola_elemento_cache(self, n):
        #se ho già la soluzione la prendo dalla cache
        #altirmenti vado avanti con la recursione
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.ricorsioni_cache+=1
            self.cache[n]=self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2)
            return self.cache[n]

    def calcola_elemento(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            self.ricorsioni+=1
            return self.calcola_elemento(n-1)+self.calcola_elemento(n-2)

if __name__=="__main__":
    N=10 # se il numero è tanto alto ci mette tanto tempo, cerchiamo di fare il calcolo in meno tempo
    fiv= Fibonacci()

    start_time = time()
    print(fiv.calcola_elemento(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")
    print(fiv.ricorsioni)

    start_time= time()
    print(fiv.calcola_elemento_cache(N))
    end_time=time()
    print(f"Elapsed time - cache: {(end_time-start_time):6f}")
    print(fiv.ricorsioni_cache)

    #start_time = time()
    #print(fiv.calcola_elemento_lru(N))
    #end_time = time()
    #print(f"Elapsed time - cache: {(end_time - start_time):6f}")