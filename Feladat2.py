def feladat_1(a):
    darab=0
    for i in range(1,a+1):
        if a%i==0:
            darab=darab+1
    if darab==4:
        return True
    else:
        return False



def feladat_2(n):
    szamok=2
    darab=0
    while darab<n:
        prim=True
        for i in range (2,szamok//2+1):
            if szamok%i==0:
                prim=False
                break
        if prim:
            darab=darab+1
        if darab==n:
            return szamok
        szamok=szamok+1


print(feladat_2(5))


def feladat_3(n):
    hatvany=1
    while n>hatvany:
        hatvany=hatvany*2
    return hatvany

def feladat_4():
    for i in range(100,1000):
        szam=i
        szamjegy1=i%10
        i=i//10
        szamjegy2=i%10
        i=i//10
        szamjegy3=i%10
        if szamjegy1!=szamjegy2 and szamjegy1!=szamjegy3 and szamjegy2!=szamjegy3:
            print(szam)
feladat_4()

def feladat_5_osztoszam(a):
    darab=2
    for i in range(2,a//2+1):
        if a%i==0:
            darab=darab+1
    return darab

def feladat_5(n):
    for i in range(1,n+1):
        darab=feladat_5_osztoszam(i)
        eroszam=True
        for j in range(1,i):
            if darab<=feladat_5_osztoszam(j):
                eroszam=False
                break
        if eroszam:
            print (i)

feladat_5(100)




