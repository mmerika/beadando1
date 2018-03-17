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

def feladat_6_szamjegy(a):
    tömb=[]
    while a>0:
        tömb.append(a%10)
        a=a//10
    return tömb
print(feladat_6_szamjegy(123))

def feladat_6(szamjegy1,szamjegy2):
    szamjegy1tömb=feladat_6_szamjegy(a)

def feladat_6_szamjegy(a):
    tömb=[]
    while a>0:
        tömb.append(a%10)
        a=a//10
    return tömb
print(feladat_6_szamjegy(123))

def feladat_7(a,b):
    tömba=feladat_6_szamjegy(a)
    tömbb=feladat_6_szamjegy(b)
    for i in range(0,len(tömba)):
        for j in range(0,len(tömbb)):
            if tömba[i]==tömbb[j]:
                return True
    return False
print(feladat_7(123,653))

def feladat_8(n):
    i=0
    osszeg=0
    while osszeg<n:
        i=i+1
        osszeg=osszeg+i
    return i

print(feladat_8(1000))

def feladat_9():
    magassag=1
    i=1
    while magassag<300:
        i=i+1
        magassag=magassag+magassag*(1/i)
    return i
feladat_9()

def feladat_10():
    try:
        sorhossz=0
        file=open("be.txt","r")
        for line in file:
            if line[0].isupper():
                if sorhossz<len(line):
                    sorhossz=len(line)
        return sorhossz
    except Error:
        print("Nem sikerült olvasni a fájlt!")
        return 0
    finally:
        file.close()

print(feladat_10())

def feladat_11():
    try:
        sorhossz = 0
        file = open("be.txt", "r")
        for line in file:
            line = line.rstrip()
            if line[len(line)-1]=="." or line[len(line)-1]=="?" or line[len(line)-1]=="!" :
                if sorhossz > len(line) or sorhossz==0:
                    sorhossz = len(line)
        return sorhossz
    except Error:
        print("Nem sikerült olvasni a fájlt!")
        return 0
    finally:
        file.close()

print(feladat_11())

def feladat_17():
    try:
        file = open("be.txt", mode="r")
        fileki=open("ki.txt", mode="w+")
        megvan=False
        for line in file:
            fileki.write(line)
            line = line.rstrip()
            szavak=line.split(" ")
            for i in range(0, len(szavak)):
                if szavak[i]==szavak[i].lower():
                    fileki.write(line)
                    megvan=True
                    break
            if megvan:
                break
    except Error:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()





