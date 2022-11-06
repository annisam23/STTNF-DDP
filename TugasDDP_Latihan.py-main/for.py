#cetak bil 1 s/d 20
angka = 20
for no in range(angka):
    no += 1
    print("Angka",no)

#cetak bil 1 s/d 20 genap
bil = 20
for no in range (bil):
    no += 1
    if(no % 2 == 0):
        print("Bilangan genap",no)

#if latihan
nama = "budi"
totalbelanja = 10000
if (totalbelanja > 8000):
    keterangan = "selamat kamu dapat hadiah"
else:
    keterangan = "blm beruntung"

#cetak data
print("Pelanggan",nama)
print("Total belanjanya :",totalbelanja,"\n",keterangan)



#nesteedloop
for i in range (5):
    for j in range (i +1):
        print("*", end="")
        print(" ")