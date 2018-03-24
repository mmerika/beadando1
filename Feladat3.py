def feladat_1():
    n=int(input(''))
    tomb=[]
    for i in range(0,n):
        a=int(input(''))
        tomb.append(a)
    for i in range(0,n-1):
        if tomb[i]==tomb[i+1]:
            print (i, i+1)

feladat_1()