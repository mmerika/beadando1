import math

def feladat_1(A,B):
    A=A-B
    B=B+A
    A=B-A
    print(A)
    print(B)

feladat_1(4,6)

def feladat_2():
    a = int(input("Kérem az első számot!"))
    b = int(input("Kérem az második számot!"))
    c = int(input("Kérem az harmadik számot!"))
    if a<b and a < c and b<c:
        print (a,b,c)
    elif a<c and a<b and c<b:
        print(a,c,b)
    elif b<a and b<c and a<c:
        print (b,a,c)
    elif b<c and b<a and c<a:
        print(b,c,a)
    elif c<a and c<b and b<a:
        print (c,b,a)
    else:
        print (c,a,b)

feladat_2()

def feladat_3(x):

    if x>-2 and x<0:
        return (2*x)
    elif x>=0 and x<2:
        return (x**2)
    elif x>2:
        return(10)
    else:
        return("erre nincs definiálva a függvény")

x = feladat_3(-10)
print(x)

def feladat_4(a,b,c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    elif c < a and c < b:
        print(c)
    if abs(a) < abs(b) and abs(c) < abs(b):
        print(b)
    elif abs(b) < abs(a) and abs(c) < abs(a):
         print(a)
    elif abs(a) < abs(c) and abs(b) < abs(c):
        print(c)

feladat_4(5,7,-5)

def feladat_5(a,b,c,d):
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

feladat_5(2,4,1,3)

def feladat_6(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a:
        print("Van ilyen háromszög!")
    else:
        print("Nincs ilyen háromszög!")

feladat_6(2, 5, 6)

def feladat_7(a,b,dh):
    K=2*(a+b)
    if K==dh:
        print("Pont elég a drótkerítés!")
    elif K>dh:
        print(K-dh,"méter drót kell még a kerítéshez")
    else:
        print(dh-K,"méterrel több drót marad a kerítés építés után")

feladat_7(5,5,18)

def feladat_13(erdemjegy):
    if erdemjegy==5:
        print("ötös")
    elif erdemjegy==4:
        print("négyes")
    elif erdemjegy==3:
        print("hármas")
    elif erdemjegy==2:
        print("kettes")
    elif erdemjegy==1:
        print("egyes")

feladat_13(4)

def feladat_14(hónap):
    if hónap==1:
        print("Január")
    elif hónap==2:
        print("Február")
    elif hónap==3:
        print("Március")
    elif hónap == 4:
        print("Április")
    elif hónap == 5:
        print("Május")
    elif hónap == 6:
        print("Június")
    elif hónap == 7:
        print("Július")
    elif hónap==8:
        print("Augusztus")
    elif hónap==9:
        print("Szeptember")
    elif hónap==10:
        print("Október")
    elif hónap==11:
        print("November")
    elif hónap==12:
        print("December")
feladat_14(10)

def feladat_12(elert,max):
    szazalek=elert/max*100
    if szazalek>=60:
       print("Sikeres")
    else:
        print("Sikertelen")
feladat_12(65,110)

def feladat_10(ev1,ev2):
    szokoevek=0;
    for i in range(ev1,ev2+1):
        if i%4==0 and i%100!=0:
            szokoevek=szokoevek+1
        if i%400==0:
            szokoevek=szokoevek+1
    print(szokoevek)

feladat_10(1990,2019)

def feladat_15(a,b):
    hanyados=0;
    while a>=b:
        hanyados=hanyados+1
        a=a-b
    return hanyados

print (feladat_15(75,15))

def feladat_16(a,b):
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b

print(feladat_16(360,225))

def feladat_17(a):
    eredeti=a
    b=0
    while a>0:
        m=a%10
        b=b*10+m
        a=a//10
    return eredeti==b
print("palindrom: ", feladat_17(101))

def feladat_18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if x%2==1:
            p=p+y
        x=x//2
        y=y+y
    return p
print (feladat_18(45,17))

def feladat_19(n):
    valasz=True
    for i in range (2,int(math.sqrt(n))):
        if n%2==0:
            valasz=False
            break
    return valasz
print (feladat_19(10))

def feladat_20(n):
    a=1
    b=0
    for i in range (1,n+1):
        print (b)
        b=a+b
        a=b-a
feladat_20(10)


def feladat_21(n):
    a = 0
    while n != 0:
        a = a * 10 + n % 10
        n = n // 10
    print(a)


feladat_21(321)


def feladat_22(x, n):
    eredmeny = 1
    while n > 0:
        if n % 2 == 1:
            eredmeny = eredmeny * x
            n = n - 1
        x = x * x
        n = n // 2
    print(eredmeny)


def feladat_23(n):
    x = 0
    y = 1
    while x < n:
        o = 0
        for i in range(1, y // 2 +1):
            if y % i == 0:
                o = o + i
        if o == y:
            x = x + 1
            print(y)
        y = y + 1


feladat_23(3)

def feladat_24():
    a=0
    b=0
    x=int(input(""))
    while x!=0:
        if x%7==5:
            a=a+1
        if x%13==7:
            b=b+1
        x=int(input(""))
    print(a,b)
feladat_24()

def  feladat_25():
    fo=int(input(""))
    km=int (input(""))
    s=fo/km
    if s<=50:
        print("Ritkán lakott.")
    elif s>50 and s<=300:
        print("Átlagos népsűrűsségű.")
    else:
       print("Sűrűn lakott.")
feladat_25()

def feladat_26():
    szoveg = input("")
    a, b = szoveg.split(" ")
    a = int(a)
    b = int(b)
    osszeg = a + b
    print(osszeg)