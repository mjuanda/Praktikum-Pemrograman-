# # Operator Aritmatika: 

# # Penjumlahan (+), Pembagian (/), Perkalian (*), 
# # pembagian dengan pembulatan ke bilangan bulat terkecilnya (//), Mosulus (%), Pemangkatan (**)  

# # Contohnya bila diberikan dua buah variabel (a dan b)

a, b = 8, 4

print ("a + b  =" ,a + b) #Penjumlahan
print ("a / b  =" ,a / b) #Pembagian 
print ("a * b  =" ,a * b) #Perkalian 
print ("a // b =",a // b) #Floor Devision
print ("a % b  =" ,a % b) #Mosulus (sisa bagi) 
print ("a**b   ="  ,a**b) #Pemangkatan 

print()

# Operator perbandingan komparasi:

'''
Contoh: jika diberikan dua buah variabel (a dan b)
Hail dari kedua variabel tersebut akan dicetak dengan tipe boolean (False or True)
'''

a, b = 8, 4
print ("a == b =",a == b)  #Equal (sama)
print ("a != b =",a != b)  #Not equal (tidak sama)   8 tidak sama dengan 4?
print ("a > b  =",a > b)   #Greater than (besar dari) 8 besar dari 4?
print ("a < b  =", a < b)  #Less than (kecil dari) 
print ("a >= b =", a >= b) #Greater than or equal to (lebih besar atau sama dari)
print ("a <= b", a <= b)   #Less than or equal to (lebih kecil atau sama dari)
print()

# Operator Logika
a = 8
print ("a = 8")
print ("Operator and -->", a < 5 and a < 10, "(8 kecil dari 5 dan 8 kecil dari 10)") 
print ("Operator or -->", a < 5 or a < 10, "(8 kecil dari 5 atau 8 kecil dari 10)")
print ("Operator not -->", not (a < 5 == a < 10), "(8 kecil dari 5 bukan 8 kecil dari 10)")
print()


laki2 = bool(1) #--> True
ciwi2 = bool(0) #--> False
dimas = laki2
zaki = laki2
adel = ciwi2
print()

print ("dimas and adel == laki2 --> ", dimas and adel == laki2) 
print ("dimas or adel == laki2 --> ", dimas or adel == laki2)
print()
print ("dimas == laki2 -->", dimas == laki2) #--> bernilai True
print ("not (dimas == ciwi2) --> ", not (dimas == laki2)) #--> Dibalikkan menjadi bernilai False
print()

#Operator Assignment

# a + =  2  -->  ekivalen a = a +  2
# a - =  2  -->  ekivalen a = a -  2
# a * =  2  -->  ekivalen a = a *  2
# a / =  2  -->  ekivalen a = a /  2
# a //=  2  -->  ekivalen a = a // 2
# a % =  2  -->  ekivalen a = a %  2
# a **=  2  -->  ekivalen a = a ** 2

a = 5

a += 2 #Penambahan
print ("a += 2  =", a ) 
a -= 2 #Pengurangan
print ("a -= 2  =", a ) 
a *= 2 #Perkalian
print ("a *= 2  =", a )
a /= 2 #Pembagian
print ("a /= 2  =", a )
a //= 2 #Floor Devision
print ("a //= 2 =", a ) 
a %= 2 #Modulus
print ("a %= 2  =", a ) 
a **= 2 #Eksponensial/perpangkatan
print ("a **= 2 =", a )

print (a)

print ()

#Operator Identitas
'''
jika keduanya sama secara literal dan sama secara lokasi memori akan menghasilkan nilai yang benar (True).
'''

x = [2,"Nurdin"]
y = [2,"Nurdin"]
z = y

# is
print ("x is y =", x is y) 
print ("x is z =",x is z)

#is not
print ("x is not y =", x is not y) 
print ("x is not z =", x is not z)
print ()

#cek lokasi memori
print ("id z", id(z))
print ("id x", id(x))
print ("id y", id(y))

print()

#Operator Membership
'''
Operator keanggotaan digunakan untuk mengecek keanggotaan suatu variabel tunggal
'''

MushleGym = ["ari","bibi", "kiki", "kuki"]
print()
print ("ari in MushleGym -->", "ari" in MushleGym)
print ("ari not in MushleGym -->","ari" not in MushleGym)
print()

Vip = [1,0]

hapus_member = (1)
if hapus_member in Vip:
    Vip.remove(hapus_member)
    print ("berhasil dihapus.")
else:
    print ("tidak ditemukan.")
print ("setelah penghapusan", Vip)

if 1 not in Vip: #False
    print (hapus_member, " tidak lagi Vip")
    print(Vip)
if 1 in Vip: #True
    print (hapus_member," masih dalam Vip")
    print(Vip)

print()
#Print Formating

'''
Guna untuk memformat hasil tampilan statement menggunakan print (f"", dan atau % )

'''
#Format untuk print formating
#:d, :kd, :f, :m.kf, :e, :m.ke

#Operator %

#%d 
# tipe data integer
a = 100
print ("modulo a = %d" % (a))
print ("modulo a = %8d" % (a))
print ("Bil 1:%d ,Bil 2:%d ,Bil 3:%d" % (10,23,50))

#%f
#tipe data float
b = 3.100000000
print("modulo b = %f" % (b)) #by default adalah 6 digit dibelakang titik
print("modulo b = %9f" % (b))#menambah/mengurangi total digit
print("modulo b = %.3f" % (b))#menambah/mengurangi digit dibelakang titik desimal
print("modulo b = %5.1f" % (b))#menambah/mengurangi digit didepan titik desimal

#%e
c= 1000000000000
print ("modulo c = %e" % (c))
print ("modulo c = %.2e" % (c))

#%s
print ("halo %s" % ("adit"))
nama = ("adit")
format_string = "halo %s"
print (format_string % nama)

print ("a + b  = %d + %.5f = %.2f" % (a, b, a+b))


# Format String (f"")

#mengkonstruksi sebuah string kedalam formating

#String
nama = "pascol"
format_str = f"hallo {nama}"
print(format_str)

#angka
angka = 300.1
format_str = f"angka {angka}"
print (format_str)

#bilangan desimal
format_str = f"Bil desimal {angka:.1f}"
print (format_str)

#bilangan ribuan
angka = 3000000
format_str = f"jutaan: {angka:,}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"

print(format_persen)
# COntoh dalam Looping
#-----------------------------------------
# nilai = 1
# if not (nilai > 100):
#     print("Nilai lebih kecil dari 100")
# elif (nilai >100):
#     print ("nilai lebih dari 100")

# data = True
# if not data:
#     print("Data tidak ada")
# elif data == False:
#     print ("Ada data")


