import copy


class XExpansion:
    def __init__(self):
        self.soluzioni=[]
        self.soluzioni_list=[]

    def calcola_list(self,input):
        self.soluzioni_list=[]
        self._ricorsione_list([],input)

    def _ricorsione_list(self,parziale: list,rimanenti:str):
        if len(rimanenti)==0:
            #print(parziale)
            self.soluzioni_list.append(copy.deepcopy(parziale)) #necessario per non modificare la lista
        else:
            if rimanenti[0]=="X":
                #faccio i due casi in cui x sia uguale a 1 o a 0
                for c in ["0","1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale,rimanenti[1:])
                    parziale.pop() # quando facciamo il pop facciamo il pop anche della soluzione

            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])


    def calcola(self,input):
        self.soluzioni=[] # dobbiamo mettere sempre a 0 la lista perchè è di classe quindi tiene conto di tutti i valori messi
        self._ricorsione("",input)

    #parziale è la soluzione parziale
    #rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione(self,parziale: str,rimanenti:str):
        if len(rimanenti)==0:
            #print(parziale)
            self.soluzioni.append(parziale)
        else:
            if rimanenti[0]=="X":
                #faccio i due casi in cui x sia uguale a 1 o a 0
                self._ricorsione(parziale + "0", rimanenti[1:])
                self._ricorsione(parziale + "1", rimanenti[1:])
            else:
                self._ricorsione(parziale + rimanenti[0], rimanenti[1:])

#========================================= ALTRO METODO ====================================================

def x_expansion2(input):
    soluzioni=[]

    #parziale è la soluzione parziale
    #rimanenti sono il resto dei caratteri da esaminare
    def ricorsione(parziale: str,rimanenti:str):
        if len(rimanenti)==0:
            #print(parziale)
            soluzioni.append(parziale)
        else:
            if rimanenti[0]=="X":
                #faccio i due casi in cui x sia uguale a 1 o a 0
                ricorsione(parziale + "0", rimanenti[1:])
                ricorsione(parziale + "1", rimanenti[1:])
            else:
                ricorsione(parziale + rimanenti[0], rimanenti[1:])

    ricorsione("",input)
    return soluzioni

if __name__=="__main__":
        sequenza="01X0X"
        xexp=XExpansion()

        #metodo con soluzioni parziali rappresentate come stringhe
        xexp.calcola(sequenza)
        print(xexp.soluzioni)

        # metodo con soluzioni parziali rappresentate come lista
        xexp.calcola_list(sequenza)
        print(xexp.soluzioni_list)