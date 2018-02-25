#1.feladat

def feladat_1(A,B):
    A=A-B
    B=B+A
    A=B-A
    print(A)
    print(B)

feladat_1(4,6)

#2.feladat

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

#3.feladat
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

#4.feladat

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

#5.feladat
def feladat_5(a,b,c,d):
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)
feladat_5(2,4,1,3)

#6.feladat

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