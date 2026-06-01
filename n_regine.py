import copy
from time import time

class Regina():
    def __init__(self,riga,colonna):
        self.riga=riga
        self.colonna=colonna

class NRegine:

    def __init__(self):
        self.n_soluzioni=0
        self.n_chiamate=0
        self.soluzioni = []



    ################## APPROCIO 2 ############################################
    #Rappresentiamo soluzione come un vettore di N regine,
    #ognugno rappresentante una regia come riga e colonna
    def solve2(self,N):
        self.n_soluzioni=0
        self.n_chiamate=0
        self.soluzioni = []

        self._ricorsione2([],N)


    #parziale è un vettore di coppie riga e colonna
    def _ricorsione2(self,parziale,N):
        self.n_chiamate+=1
        if len(parziale)==N:
            #if self._is_soluzione(parziale):
            #    self.n_soluzioni+=1
            #    print(parziale)

            if self._is_nuova_soluzione(parziale):
                self.n_soluzioni+=1
                self.soluzioni.append(copy.deepcopy(parziale))
            #print(parziale)
        else:
            for riga in range(N):
                for colonna in range(N):
                    #verifico se la nuova regina sia ammissibile
                    nuova_regina=(riga,colonna)
                    if self._step_is_valid(nuova_regina, parziale):
                        parziale.append(nuova_regina)
                        self._ricorsione2(parziale,N)
                        #backtracking
                        parziale.pop()
     #confrontiamo la soluzione potenziale con tutte quelle già trovate
    #se è diversa restituiamo True, altrimenti False
    def _is_nuova_soluzione(self,soluzione_potenziale) ->bool:
        N=len(soluzione_potenziale)
        for soluzione in self.soluzioni:
            counter=0
            for regina in soluzione_potenziale:
                if regina in soluzione:
                    counter+=1
            if counter==N:
                return False
        return True

    #funzione che controll se la nuova regina da inserire sia ammissibile rispetto alla soluzione parziale costruita finora
    def _step_is_valid(self,nuova_regina,parziale) ->bool:
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina,regina):
                return False
        return True

    # funzione che prende due regine e restituisce true se non si possono attaccaere
    def _is_pair_admissible(self,regina1,regina2)->bool:
        #1) verifico la riga. Se non va bene, return False
        if regina1[0]==regina2[0]:
            return False
        #2) verifico la colonna. Se non va bene, return False
        if regina1[1]==regina2[1]:
            return False
        #3)verifico la diagonale 1. Se non va bene, return False
        #la differenza di indici è una costante
        if (regina1[0]-regina1[1])==(regina2[0]-regina2[1]):
            return False
        #4)verifico la diagonale 2. Se non va bene, return False
        #la somma degli indici è una costante
        if (regina1[0]+regina1[1])==(regina2[0]+regina2[1]):
            return False
        #5)Ho passato tutti i controlli, return True
        return True

    #metodo che data una possibile soluzione verifica che sia ammissibile
    def _is_soluzione(self,soluzione_possibile) ->bool:
        for i in range(len(soluzione_possibile)-1):
            for j in range(i+1,len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i],soluzione_possibile[j]):
                    return False
        return True


if __name__ == '__main__':
    nreg= NRegine()
    start_time=time()
    nreg.solve2(4)
    end_time=time()


    print(f"Elapsed time= {end_time-start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili ")
    print(f"Chiamate effetuate: {nreg.n_chiamate}")
    print(nreg.soluzioni)