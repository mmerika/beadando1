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
    except IOError:
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
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
        return 0
    finally:
        file.close()

print(feladat_11())

def feladat_12():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        fileki= open("ki.txt", mode="w+")
        max=0
        akt=0
        elozo=0
        for line in file:
            line = line.rstrip()
            if akt==0:
                elozo=int(line)
                akt=akt+1
            else:
                if int(line)==elozo:
                    akt=akt+1
                else:
                    if akt>max:
                        max=akt
                    akt=1
                    elozo=int(line)
        if akt>max:
            max=akt
        if max>=elozo:
            fileki.write("IGEN")
        else:
            fileki.write("NEM")
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

feladat_12()

def feladat_13():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        elozo=0
        db=0
        tomb=[]
        for line in file:
            line = line.rstrip()
            if elozo!=0:
                tomb.append(abs(elozo-int(line)))
            elozo=int(line)
        for i in range(0, len(tomb)):
            if elozo>=tomb[i]:
                db=db+1
        print (db)
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()

feladat_13()

def feladat_14():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        fileki = open("ki.txt", mode="w+")
        for line in file:
            line = line.rstrip()
            leghosszabb = 0
            for i in range(0, len(line) // 2):
                if line[i] == line[len(line) - 1 - i]:
                    leghosszabb = leghosszabb + 1
                else:
                    break
            fileki.write(str(leghosszabb) + "\n")
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

feladat_14()

def feladat_15():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        fileki = open("ki.txt", mode="w+")
        for line in file:
            line = line.rstrip()
            if line.strip()=="":
                break
            fileki.write(line+"\n")
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

feladat_15()

def feladat_16():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        fileki = open("ki.txt", mode="w+")
        for line in file:
            line = line.rstrip()
            if line==line.upper():
                fileki.write(line+"\n")
                break
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

feladat_16()

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
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

def feladat_18():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        for line in file:
            line = line.rstrip()
            adatok=line.split(" ")
            eredmenyek=adatok[3].split(":")
            if int(eredmenyek[1])>int(eredmenyek[0]):
                print(adatok[2])
            else:
                print(adatok[0])
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()

feladat_18()

def feladat_19():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        legtobben = 0
        weboldal = ""
        for line in file:
            line = line.rstrip()
            adat=line.split(" ")
            if int(adat[1]) > legtobben:
                legtobben = int(adat[1])
                weboldal = adat[0]
        print(weboldal)
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()

feladat_19()

def feladat_20():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        legtobben = 0
        varosnev = ""
        for line in file:
            line = line.rstrip()
            adat=line.split(";")
            if int(adat[2]) > legtobben:
                legtobben = int(adat[2])
                varosnev = adat[0]
        print(varosnev)
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()

feladat_20()

def feladat_21():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        fileki = open("ki.txt", mode="w+")
        for line in file:
            line = line.rstrip()
            adat=line.split(";")
            osszpont=0
            for i in range(1, len(adat)):
                osszpont=osszpont+int(adat[i])
            fileki.write(adat[0] + " " + str(osszpont) + "\n")
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

feladat_21()

def feladat_22():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        fileki = open("ki.txt", mode="w+")
        ido=0.0
        nev=""
        for line in file:
            line = line.rstrip()
            adat=line.split(";")
            if ido==0.0 or ido>float(adat[2]):
                ido=float(adat[2])
                nev=adat[0]
        fileki.write(nev + "\n")
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

feladat_22()

def feladat_23():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        elozotavolsag=0
        for line in file:
            line = line.rstrip()
            if elozotavolsag>int(line):
                print("NO")
                return
            else:
                elozotavolsag=int(line)
        print ("YES")
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()

feladat_23()

def feladat_24():
    try:
        file = open("be.txt", mode="r", encoding="UTF-8")
        n = int(file.readline())
        teknoc = file.readline().split(" ")
        csiga = file.readline().split(" ")
        teknocut = 0
        csigaut = 0
        for i in range(0, n):
            teknocut = teknocut + int(teknoc[i])
            csigaut = csigaut + int(csiga[i])
        if csigaut > teknocut:
            print(csigaut * 2)
            print("SNAIL ")
        elif teknocut > csigaut:
            print(teknocut * 2)
            print("TURTLE")
        else:
            print(csigaut * 2)
            print("DRAW")

    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()

feladat_24()

def feladat_25():
    try:
        file = open("szotar.txt", mode="r", encoding="UTF-8")
        n = int(file.readline())
        angolszavak = []
        magyarszavak = []
        for i in range(0, n):
            line = file.readline().rstrip()
            szavak = line.split(":")
            angolszavak.append(szavak[0])
            magyarszavak.append(szavak[1])
        print(len(angolszavak))
        print(len(magyarszavak))
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()

feladat_25()

def feladat_26():
    try:
        a = input("fáljnév1")
        b = input("fáljnév2")
        file = open(a, mode="r", encoding="UTF-8")
        file2 = open(b, mode="r", encoding="UTF-8")
        fileki = open("ki.txt", mode="w+", encoding="UTF-8")
        db1 = 0
        db2 = 0
        for line in file:
            line = line.rstrip()
            db1=db1+1
        for line in file2:
            db2=db2+2
        fileki.write(db1+" "+db2)
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        file2.close()
        fileki.close()

feladat_26()

def feladat_27():
    try:
        a = input("fáljnév1")
        file = open(a, mode="r", encoding="UTF-8")
        fileki = open("ki.txt", mode="w+", encoding="UTF-8")
        legkevesebb = 500
        nev = ""
        for line in file:
            line = line.rstrip()
            adat = line.split(":")
            szerzok = adat[1].split(",")
            if len(szerzok) < legkevesebb:
                legkevesebb = len(szerzok)
                nev = adat[0]
        fileki.write(nev)
    except IOError:
        print("Nem sikerült olvasni a fájlt!")
    finally:
        file.close()
        fileki.close()

feladat_27()