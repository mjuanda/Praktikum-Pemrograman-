#
# NIM   : 210102078
# NAMA  : Agung Laksono Yudho
# 
# TUGAS MODUL 05
#

# Konstanta
# Gaya luar (kN ke N)
P = 10 * 1000
# Panjang balok (m)
L = 5
# Posisi gaya luar (m)
a = 3
# Modul elastisitas (GPa ke Pa)
E = 200 * 10**9
# momen inersia (m^4)
I = 25 * 10**-5
# asumsi jarak beban dari ujung B
b = L - a

# Titik-titik yang ditentukan
titik = [0, L/10, 2*L/10, 3*L/10, 4*L/10, 5*L/10, 6*L/10, 7*L/10, 8*L/10, 9*L/10, L]

# Perhitungan
for x in titik:
    if 0 <= x <= a:
        defleksi = (P * b / (6 * E * I * L)
                    ) * x * (L**2 - x**2 - b**2
                    )
    elif a <= x <= L:
        defleksi = (P * b / (6 * E * I * L)
                    ) * (L / b * (x - a)**3 + (L**2 - b**2) * x - x**3
                    )
    else:
        defleksi = (x < 0 | x > L)
# Cetak hasil
    print(f"Defleksi pada x sebesar {x:.1f} m = {defleksi:.6f} m\n")


