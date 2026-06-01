def binomial(n,m):
    if n<0 or m<0 or m>n:
        print("Inserire numeri positivi e in modo che n sia maggiore o uguale  a m!")
    if n==m or m==0:
        return 1
    else:
        return binomial(n-1,m-1) + binomial(n-1,m)

if __name__=="__main__":
    n=5
    m=3
    print(binomial(n,m))