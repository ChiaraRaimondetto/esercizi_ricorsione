import copy
from functools import lru_cache


def anagrammi(parola):
    soluzioni=[]
    ricorsione([],parola,soluzioni)
    return soluzioni
def ricorsione(parziale: list,rimanenti:str,soluzioni:list) -> list: #diciamo che loutput deve essere una lista
    if len(rimanenti)==0 :
        soluzioni.append(copy.deepcopy(parziale))
    else:
        for i in range(len(rimanenti)):
            parziale.append(rimanenti[i])
            nuovi_rimanenti=rimanenti [:i] + rimanenti[i+1:]
            ricorsione(parziale,nuovi_rimanenti,soluzioni)
            parziale.pop()



def anagrammi_str(parola):
    soluzioni=set()
    ricorsione_str("",parola,soluzioni)
    return soluzioni

def ricorsione_str(parziale: str,rimanenti:str,soluzioni:list) : #diciamo che loutput deve essere una lista
    if len(rimanenti)==0 :
        soluzioni.add(copy.deepcopy(parziale))
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti=rimanenti [:i] + rimanenti[i+1:]
            ricorsione_str(parziale + rimanenti[i],nuovi_rimanenti,soluzioni)


def anagrammi_str2(parola):
    ricorsione_str2("",parola)

@lru_cache(maxsize=None)# mi restituisce una sola volta le combinazioni uguali
def ricorsione_str2(parziale: str,rimanenti:str) :
    if len(rimanenti)==0:
        print(parziale)
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti=rimanenti [:i] + rimanenti[i+1:]
            ricorsione_str2(parziale + rimanenti[i],nuovi_rimanenti)


if __name__=="__main__":
    print(anagrammi('casa'))
    print(anagrammi_str2('aaaa'))