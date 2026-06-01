import copy
from time import time


class Quadrato_magico():
    def __init__(self,N):
        self.N=N
        self.n_chiamate=0
        self.n_soluzioni=0
        self.soluzioni=[]

     #soluzione rappresentata da un vettore di N**2 elementi,
    #ogni elemento rapprresenta una cella del quadrato, ed il suo valore è il numero
    #che mettiamo nella cella
    def risolvi_quadrato(self):
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []
        rimanenti=set(range(1,self.N*self.N+1))
        self._ricorsione([],rimanenti)

    def _ricorsione(self,parziale,rimanenti):
        self.n_chiamate +=1
        if len(parziale)==self.N*self.N:
            if self._is_valid(parziale):

                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
            #print(parziale)
        else:
            for numero in rimanenti:
                parziale.append(numero)
                if self._is_parziale_valid(parziale ):
                    #rimanenti.remove(numero) ma conviene fare una copia
                    nuovi_rimanenti=copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(numero)
                    self._ricorsione(parziale,nuovi_rimanenti)
                parziale.pop()

    def _is_parziale_valid(self, parziale):
        numero_magico = self.N * (self.N * self.N + 1) / 2

        # 1 controllare righe
        n_righe_completate=len(parziale)//self.N
        for id_riga in range(n_righe_completate):
            riga = parziale[id_riga * self.N:(id_riga + 1) * self.N]
            if sum(riga) != numero_magico:
                return False

        # 2 contrlollare colonne
        n_colonne_completate=max(len(parziale)-self.N*(self.N-1),0)
        for id_colonna in range(n_colonne_completate):
            col = parziale[id_colonna:(self.N - 1) * self.N + id_colonna + 1:self.N]
            if sum(col) != numero_magico:
                return False

        # 3 controllare diagonale 1
        #diagonale1 = parziale[0:self.N ** 2:self.N + 1]
        #if sum(diagonale1) != numero_magico:
        #    return False

        # 4 controllare diagonale 2
        #somma = 0
        #for indice in range(self.N):
        #    somma += parziale[indice * self.N + (self.N - 1 - indice)]
        #    if somma != numero_magico:
        #        return False
        # 5 ritornare True se passa i controlli
        return True

    def _is_valid(self,potenziale_soluzione):
        numero_magico=self.N*(self.N*self.N+1)/2
        #1 controllare righe
        for id_riga in range(self.N):
            riga=potenziale_soluzione[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga)!=numero_magico:
                return False

        #2 contrlollare colonne
        for id_colonna in range(self.N):
            col=potenziale_soluzione[id_colonna:(self.N-1)*self.N+id_colonna + 1:self.N]
            if sum(col)!=numero_magico:
                return False

        #3 controllare diagonale 1
        diagonale1=potenziale_soluzione[0:self.N**2:self.N+1]
        if sum(diagonale1)!=numero_magico:
            return False

        #4 controllare diagonale 2
        somma=0
        for indice in range(self.N):
            somma+=potenziale_soluzione[indice*self.N+ (self.N-1-indice)]
        if somma!=numero_magico:
            return False
        #5 ritornare True se passa i controlli
        return True

    def stampa_quadrato(self,soluzione):
        print("------------")
        for riga in range(self.N):
            print(soluzione[riga*self.N:(riga+1)*self.N])
        print("------------")

if __name__ == '__main__':
    qm=Quadrato_magico(3)
    start_time=time()
    qm.risolvi_quadrato()
    end_time=time()

    print(f"Tempo impiegato= {end_time-start_time}")
    print(f"Chiamate effetuate = {qm.n_chiamate}")
    print(f"Soluzione trovate = {qm.n_soluzioni}")
    for soluzione in qm.soluzioni:
        qm.stampa_quadrato(soluzione)