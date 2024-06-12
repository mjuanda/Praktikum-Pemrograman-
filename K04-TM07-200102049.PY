#
#KELOMPOK   : Kelompok 07
#NAMA       : Rahmat Eldiyansyah
#
#TUGAS MODUL : 07
import cmath

###

def akar_akar_kuadrat (a = 2, b = 5, c = 3):
    D = b**2 - 4*a*c
    return D

###

D = lambda x, a = 2, b = 3: c*x + b 
print(D)

###
a = float(input("koefesien x**2 ="))
b = float(input("koefesien x ="))
c = float(input("konstanta ="))
print(f" persamaan kuadrat : {a:.2f}x**2 + {b:.2f}x + {c:.2f} = 0")

D = b**2 - 4*a*c
print(f"\n Nilai determinan D = {D:.2f}")


def akar_akar_kuadrat (a = 2, b = 5, c = 3):
    D = b**2 - 4*a*c

x_1st_term = (-b + cmath.sqrt(D))/(2*a)
x_2nd_term = (-b - cmath.sqrt(D))/(2*a)
    

if D >= 0 :
    if D==0:
        jenis = "akar ril kembar"
    else:
        jenis = "akar-akar ril berbeda"
        x1 = f"x1 = {x_1st_term + x_2nd_term:.4f}"
        x2 = f"x2 = {x_1st_term - x_2nd_term:.4f}"
else :
    jenis = "akar kompleks dan konyugatnya"
    x1 = f"x1 = {x_1st_term:.4f} + {x_2nd_term:.4f}i"
    x2 = f"x2 = {x_1st_term:.4f} - {x_2nd_term:.4f}i"
print(f"akar-akar :")
print(f"\njenis akar : {jenis}")
print(f"akar-akar :\n\t{x1}\n\t{x2}")

###

a = 2
b = 5
c = float(input("konstanta ="))
print(f" persamaan kuadrat : {a:.2f}x**2 + {b:.2f}x + {c:.2f} = 0")

D = b**2 - 4*a*c
print(f"\n Nilai determinan D = {D:.2f}")


def akar_akar_kuadrat (a = 2, b = 5, c = 3):
    D = b**2 - 4*a*c

x_1st_term = (-b + cmath.sqrt(D))/(2*a)
x_2nd_term = (-b - cmath.sqrt(D))/(2*a)
    

if D >= 0 :
    if D==0:
        jenis = "akar ril kembar"
    else:
        jenis = "akar-akar ril berbeda"
        x1 = f"x1 = {x_1st_term + x_2nd_term:.4f}"
        x2 = f"x2 = {x_1st_term - x_2nd_term:.4f}"
else :
    jenis = "akar kompleks dan konyugatnya"
    x1 = f"x1 = {x_1st_term:.4f} + {x_2nd_term:.4f}i"
    x2 = f"x2 = {x_1st_term:.4f} - {x_2nd_term:.4f}i"
print(f"akar-akar :")
print(f"\njenis akar : {jenis}")
print(f"akar-akar :\n\t{x1}\n\t{x2}")




