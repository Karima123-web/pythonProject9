#donnée
Pf=100
F1=0
F2=0
F3=100
F4=0
F5=0
z1=0.3
z2=0.3
z3=0.4
v1=0
v2=150
#initier V
v3=float(input("estimez v3 "))
v4=float(input("estimez v4 "))
v5=float(input("estimez v5 "))
#initier T
t1=float(input("estimez t1 "))
t2=float(input("estimez t2 "))
t3=float(input("estimez t3 "))
t4=float(input("estimez t4 "))
t5=float(input("estimez t5 "))
#premier élément
#calculer A
A12=int(v2)+int(F1)-50
print ("A12= ", A12)
A13=int(v3)+int(F1)+int(F2)-50
print ("A13= ", A13)
A14=int(v4)+int(F1)+int(F2)+int(F3)-50
print ("A14= ", A14)
A15=int(v5)+int(F1)+int(F2)+int(F3)+int(F4)-50
print ("A15= ", A15)
#les constantes d'antoine et
A1=6.8196
B1=785
C1=247
#calculer P
P11 = float((10 ** (A1 - (B1 / (C1 + (t1 - 32) * (5 / 9))))) / 51.715)
print("P11=", P11)
P12 = float((10 ** (A1 - (B1 / (C1 + (t2 - 32) * (5 / 9))))) / 51.715)
print("P31=", P12)
P13 = float((10 ** (A1 - (B1 / (C1 + (t3 - 32) * (5 / 9))))) / 51.715)
print("P13=", P13)
P14 = float((10 ** (A1 - (B1 / (C1 + (t4 - 32) * (5 / 9))))) / 51.715)
print("P14=", P14)
P15 = float((10 ** (A1 - (B1 / (C1 + (t5 - 32) * (5 / 9))))) / 51.715)
print("P15=", P15)
#calculer  K
K11 = P11 / Pf
print("K11=", K11)
K12 = P12 / Pf
print("K12=", K12)
K13 = P13 / Pf
print("K13=", K13)
K14 = P14 / Pf
print("K14=", K14)
K15 = P15 / Pf
print("K15=",K15)
#calculer B
B11=-(v2+int(F1)+v1*K11)
print("B11=", B11)
B12=-(v3+int(F1)+int(F2)-50+v2*K12)
print("B12=", B12)
B13=-(v4+int(F1)+int(F2)+int(F3)-50+v3*K13)
print("B13=", B13)
B14=-(v5+int(F1)+int(F2)+int(F3)+int(F4)-50+v4*K14)
print("B14=", B14)
B15=-(0+int(F1)+int(F2)+int(F3)+int(F4)+int(F5)-50+v5*K15)
print("B15=", B15)
#calculer C
C11=v2*K12
print("C11=", C11)
C12=v3*K13
print("C12=", C12)
C13=v4*K14
print("C13=", C13)
C14=v5*K15
print("C14=", C14)
#calculer D
D11=0
print("D11=", D11)
D12=0
print("D12=", D12)
D13=-F3*z1
print ("D13=", D13)
D14=0
print("D14=", D14)
D15=0
print("D15=", D15)
#matrice
import numpy as np
M1= np.array([[B11,C11,0,0,0],
             [A12,B12,C12,0,0],
             [0,A13,B13,C13,0],
             [0,0,A14,B14,C14],
             [0,0,0,A15,B15]],dtype=float)
print("M1=", M1)
#résultat
R1= np.array([0,0,D13,0,0],dtype=float)
print("R1=",R1)
#valeurs de x
x1=np.linalg.solve(M1,R1)
print("x1=", x1)
#deuxiéme élément
#calculer A
A22=int(v2)+int(F1)-50
print ("A22= ", A22)
A23=int(v3)+int(F1)+int(F2)-50
print ("A23= ", A23)
A24=int(v4)+int(F1)+int(F2)+int(F3)-50
print ("A24= ", A24)
A25=int(v5)+int(F1)+int(F2)+int(F3)+int(F4)-50
print ("A25= ", A25)
#constantes d'antoine
A2=6.78866
B2=899.617
C2=241.942
#calculer P
P21 = float((10 ** (A2 - (B2 / (C2 + (t1 - 32) * (5 / 9))))) / 51.715)
print("P21=", P21)
P22 = float((10 ** (A2 - (B2 / (C2 + (t2 - 32) * (5 / 9))))) / 51.715)
print("P22=", P22)
P23 = float((10 ** (A2 - (B2 / (C2 + (t3 - 32) * (5 / 9))))) / 51.715)
print("P23=", P23)
P24 = float((10 ** (A2 - (B2 / (C2 + (t4 - 32) * (5 / 9))))) / 51.715)
print("P24=", P24)
P25 = float((10** (A2 - (B2 / (C2 + (t5 - 32) * (5 / 9))))) / 51.715)
print("P25=", P25)
#calculer K
K21 = P21 / Pf
print("K21=", K21)
K22 = P22 / Pf
print("K22=", K22)
K23 = P23 / Pf
print("K23=", K23)
K24 = P24 / Pf
print("K24=", K24)
K25 = P25 / Pf
print("K25=",K25)
#calculer B
B21=-(v2+int(F1)+v1*K21)
print("B21=", B21)
B22=-(v3+int(F1)+int(F2)-50+v2*K22)
print("B22=", B22)
B23=-(v4+int(F1)+int(F2)+int(F3)-50+v3*K23)
print("B23=", B23)
B24=-(v5+int(F1)+int(F2)+int(F3)+int(F4)-50+v4*K24)
print("B24=", B24)
B25=-(0+int(F1)+int(F2)+int(F3)+int(F4)+int(F5)-50+v5*K25)
print("B25=", B25)
#calculer C
C21=v2*K22
print("C21=", C21)
C22=v3*K23
print("C22=", C22)
C23=v4*K24
print("C23=", C23)
C24=v5*K25
print("C24=", C24)
#calculer D
D21=0
print("D21=", D21)
D22=0
print("D22=", D22)
D23=-F3*z2
print ("D23=", D23)
D24=0
print("D24=", D24)
D25=0
print("D25=", D25)
#matrice
import numpy as np
M2= np.array([[B21,C21,0,0,0],
             [A22,B22,C22,0,0],
             [0,A23,B23,C23,0],
             [0,0,A24,B24,C24],
             [0,0,0,A25,B25]],dtype=float)
print("M2=", M2)
#résultat
R2= np.array([0,0,D23,0,0],dtype=float)
print("R2=",R2)
#valeurs de x
x2=np.linalg.solve(M2,R2)
print("x2=", x2)
#élément trois
#calculer A
A32=int(v2)+int(F1)-50
print ("A32= ", A32)
A33=int(v3)+int(F1)+int(F2)-50
print ("A33= ", A33)
A34=int(v4)+int(F1)+int(F2)+int(F3)-50
print ("A34= ", A34)
A35=int(v5)+int(F1)+int(F2)+int(F3)+int(F4)-50
print ("A35= ", A35)
#constante d'antoine
A3=6.84471
B3=1060.733
C3=231.541
#calculer P
P31 = float((10 ** (A3 - (B3 / (C3 + (t1 - 32) * (5 / 9))))) / 51.715)
print("P31=", P31)
P32 = float((10 ** (A3 - (B3 / (C3 + (t2 - 32) * (5 / 9))))) / 51.715)
print("P32=", P32)
P33 = float((10 ** (A3 - (B3 / (C3 + (t3 - 32) * (5 / 9))))) / 51.715)
print("P33=", P33)
P34 = float((10 ** (A3 - (B3 / (C3 + (t4 - 32) * (5 / 9))))) / 51.715)
print("P34=", P34)
P35 = float((10 ** (A3 - (B3 / (C3 + (t5 - 32) * (5 / 9))))) / 51.715)
print("P25=", P35)
#calculer K
K31 = P31 / Pf
print("K31=", K31)
K32 = P32 / Pf
print("K32=", K32)
K33 = P33 / Pf
print("K33=", K33)
K34 = P34 / Pf
print("K34=", K34)
K35 = P35 / Pf
print("K35=",K35)
#calcule de B
B31=-(v2+int(F1)+v1*K31)
print("B31=", B31)
B32=-(v3+int(F1)+int(F2)-50+v2*K32)
print("B32=", B32)
B33=-(v4+int(F1)+int(F2)+int(F3)-50+v3*K33)
print("B33=", B33)
B34=-(v5+int(F1)+int(F2)+int(F3)+int(F4)-50+v4*K34)
print("B34=", B34)
B35=-(0+int(F1)+int(F2)+int(F3)+int(F4)+int(F5)-50+v5*K35)
print("B35=", B35)
#calcule de C
C31=v2*K32
print("C31=", C31)
C32=v3*K33
print("C32=", C32)
C33=v4*K34
print("C33=", C33)
C34=v5*K35
print("C34=", C34)
#calcule de D
D31=0
print("D31=", D31)
D32=0
print("D32=", D32)
D33=-F3*z3
print ("D33=", D33)
D34=0
print("D34=", D34)
D35=0
print("D35=", D35)
#matrice
import numpy as np
M3= np.array([[B31,C31,0,0,0],
             [A32,B32,C32,0,0],
             [0,A33,B33,C33,0],
             [0,0,A34,B34,C34],
             [0,0,0,A35,B35]],dtype=float)
print("M3=", M3)
#résultat
R3= np.array([0,0,D33,0,0],dtype=float)
print("R3=",R3)
#valeur de x
x3=np.linalg.solve(M3,R3)
print("x3=", x3)
#normalisation des x
print("normalisation des x : ")
#élément 1
som1=x1[0]+x2[0]+x3[0]
print("somme1 = ", som1)
if som1 != 1 :
    X11 = x1[0] / (x1[0] + x2[0] + x3[0])
    X21 = x2[0] / (x1[0] + x2[0] + x3[0])
    X31 = x3[0] / (x1[0] + x2[0] + x3[0])
    print("X11 = ", X11)
    print("X21 = ", X21)
    print("X31 = ", X31)
    S1 = X11 + X21 + X31
    print("la somme1 normalisé = ", S1)
#élément 2
som2=x1[1]+x2[1]+x3[1]
print("somme2 = ", som2)
if som2 != 1 :
    X12 = x1[1] / (x1[1] + x2[1] + x3[1])
    X22 = x2[1] / (x1[1] + x2[1] + x3[1])
    X32 = x3[1] / (x1[1] + x2[1] + x3[1])
    print("X12 = ", X12)
    print("X22 = ", X22)
    print("X32 = ", X32)
    S2 = X12 + X22 + X32
    print("la somme2 normalisé = ", S2)
    # élément 3
    som3 = x1[2] + x2[2] + x3[2]
    print("somme3 = ", som3)
    if som3 != 1:
        X13 = x1[2] / (x1[2] + x2[2] + x3[2])
        X23 = x2[2] / (x1[2] + x2[2] + x3[2])
        X33 = x3[2] / (x1[2] + x2[2] + x3[2])
        print("X13 = ", X13)
        print("X23 = ", X23)
        print("X33 = ", X33)
        S3 = X13 + X23 + X33
        print("la somme3 normalisé = ", S3)
    som4 = x1[3] + x2[3] + x3[3]
    print("somme4 = ", som4)
    if som4 != 1:
        X14 = x1[3] / (x1[3] + x2[3] + x3[3])
        X24 = x2[3] / (x1[3] + x2[3] + x3[3])
        X34 = x3[3] / (x1[3] + x2[3] + x3[3])
        print("X14 = ", X14)
        print("X24 = ", X24)
        print("X34 = ", X34)
        S4 = X14 + X24 + X34
        print("la somme4 normalisé = ", S4)
    som5 = x1[4] + x2[4] + x3[4]
    print("somme5 = ", som5)
    if som5 != 1:
        X15 = x1[4] / (x1[4] + x2[4] + x3[4])
        X25 = x2[4] / (x1[4] + x2[4] + x3[4])
        X35 = x3[4] / (x1[4] + x2[4] + x3[4])
        print("X15 = ", X15)
        print("X25 = ", X25)
        print("X35 = ", X35)
        S5 = X15 + X25 + X35
        print("la somme5 normalisé = ", S5)
    # calcule de KiXij
    from scipy.optimize import fsolve
    def func1(T):
        a = (X11 * ((10 ** (A1 - B1 / (C1 + (T - 32) * 5 / 9))) / 5171.5) +
            X21 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) +
            X31 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) -1)
        return a
    T1 = fsolve(func1, [1])
    print("tepérature1 = ",T1)
    from scipy.optimize import fsolve
    def func2(T):
        b = (X12 * ((10 ** (A1 - B1 / (C1 + (T - 32) * 5 / 9))) / 5171.5) +
            X22 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) +
            X32 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
        return b
    T2 = fsolve(func2, [1])
    print("tepérature2 = ",T2)
    from scipy.optimize import fsolve
    def func3(T):
        c = (X13 * ((10 ** (A1 - B1 / (C1 + (T - 32) * 5 / 9))) / 5171.5) +
            X23 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) +
            X33 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
        return c
    T3 = fsolve(func3, [1])
    print("tepérature3 = ",T3)
    from scipy.optimize import fsolve
    def func4(T):
        d = (X14 * ((10 ** (A1 - B1 / (C1 + (T - 32) * 5 / 9))) / 5171.5) +
            X24 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) +
            X34 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
        return d
    T4 = fsolve(func4, [1])
    print("tepérature4 = ",T4)
    from scipy.optimize import fsolve
    def func5(T):
        e = (X15 * ((10 ** (A1 - B1 / (C1 + (T - 32) * 5 / 9))) / 5171.5) +
            X25 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) +
            X35 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
        return e
    T5 = fsolve(func5, [1])
    print("tepérature5 = ", T5)
    a = (X11 * ((10 ** (A1 - B1 / (C1 + (T1 - 32) * 5 / 9))) / 5171.5) +
         X21 * ((10 ** (A2 - B2 / (C2 + (T1 - 32) * 5 / 9))) / 5171.5) +
         X31 * ((10 ** (A3 - B3 / (C3 + (T1 - 32) * 5 / 9))) / 5171.5) - 1)
    print("K1*Xi1 - 1 = ", a)
    b = (X12 * ((10 ** (A1 - B1 / (C1 + (T2 - 32) * 5 / 9))) / 5171.5) +
         X22 * ((10 ** (A2 - B2 / (C2 + (T2 - 32) * 5 / 9))) / 5171.5) +
         X32 * ((10 ** (A3 - B3 / (C3 + (T2 - 32) * 5 / 9))) / 5171.5) - 1)
    print("K2*Xi2 - 1 = ", b)
    c = (X13 * ((10 ** (A1 - B1 / (C1 + (T3 - 32) * 5 / 9))) / 5171.5) +
         X23 * ((10 ** (A2 - B2 / (C2 + (T3 - 32) * 5 / 9))) / 5171.5) +
         X33 * ((10 ** (A3 - B3 / (C3 + (T3 - 32) * 5 / 9))) / 5171.5) - 1)
    print("K3*X13 - 1 = ", c)
    d = (X14 * ((10 ** (A1 - B1 / (C1 + (T4 - 32) * 5 / 9))) / 5171.5) +
         X24 * ((10 ** (A2 - B2 / (C2 + (T4 - 32) * 5 / 9))) / 5171.5) +
         X34 * ((10 ** (A3 - B3 / (C3 + (T4 - 32) * 5 / 9))) / 5171.5) - 1)
    print("K4*Xi4 - 1 = ", d)
    e = (X15 * ((10 ** (A1 - B1 / (C1 + (T5 - 32) * 5 / 9))) / 5171.5) +
         X25 * ((10 ** (A2 - B2 / (C2 + (T5 - 32) * 5 / 9))) / 5171.5) +
         X35 * ((10 ** (A3 - B3 / (C3 + (T5 - 32) * 5 / 9))) / 5171.5) - 1)
    print("K5*Xi5 - 1 = ", e)
    # Profil de la température
    import numpy as np
    import matplotlib.pyplot as plt
    y = np.array([T1, T2, T3, T4, T5])
    x = np.array([5, 4, 3, 2, 1])
    plt.ylabel('la température')
    plt.xlabel("les étages ")
    plt.plot(x, y, "r--", label="N=f(T)")
    plt.legend()
    plt.show()
    #Profil de la concentration dans la phase liquide
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.array([X11, X12, X13,X14,X15])
    x2 = np.array([X21, X22, X23,X24,X25])
    x3 = np.array([X31, X32, X33,X34,X35])
    y = np.array([1,2,3,4,5])
    plt.ylabel('les étages ')
    plt.xlabel("les fractions molaires x phase liquide")
    plt.plot( x,y,"r--", label="élément 1")
    plt.plot(x2,y,"b--",label="élément 2")
    plt.plot(x3, y,"y--",label="élément 3")
    plt.legend()
    plt.show()
    #les fractions de la vapeurs
    print(" les fractions yi")
    print("pour l'élément 1")
    y11=K11*X11
    print("y11 = ",y11)
    y12=K12*X12
    print("y12 = ",y12)
    y13=K13*X13
    print("y13 = ",y13)
    y14=K14*X14
    print("y14 = ",y14)
    y15=K15*X15
    print("y15 = ",y15)
    print("pour l'élément 2")
    y21=K21*X21
    print("y21 = ", y21)
    y22=K22*X22
    print("y22 = ", y22)
    y23=K23*X23
    print("y23 = ", y23)
    y24=K24*X24
    print("y24 = ", y24)
    y25=K25*X25
    print("y25",y25)
    print("pour l'élément 3")
    y31=K31*X31
    print("y31 =", y31)
    y32=K32*X32
    print("y32 = ", y32)
    y33=K33*X33
    print("y33 = ", y33)
    y34=K34*X34
    print("y34 = ", y34)
    y35=K35*X35
    print("y35 = ",y35)
    #Profil de la concentration dans la phase gaz
    import numpy as np
    import matplotlib.pyplot as plt
    dy=np.array([y11,y12,y13,y14,y15])
    dy2=np.array([y21,y22,y23,y24,y25])
    dy3=np.array([y31,y32,y33,y34,y35])
    y = np.array([1, 2, 3,4,5])
    plt.plot(dy, y,"r--", label="element 1")
    plt.plot(dy2,y,"b--",label="element 2")
    plt.plot(dy3, y,"y--",label="element 3")
    plt.ylabel('les etages ')
    plt.xlabel("les fractions molaires y phase vap")
    plt.legend()
    plt.show()
