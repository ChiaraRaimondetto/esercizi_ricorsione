from time import sleep


def countdown(n):
    #ITERATIVO
    while n>=0:
        print(n)
        sleep(1) #fare una pausa di 1 sec
        n-=1

def countdown_recursive(n):
   #RECORSIVO
    if n==0:
        print("Stop")
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)




if __name__ == '__main__':
    N=10 #devo controllare se N è un numero intero
    #countdown(N)
    countdown_recursive(N)
