print('Nama         : ANNISA MAULIDA RAHMA')
print('Nim          : 0110221070')
print('Kelas        : TI03(SELASA SORE)')

#Lingkaran
print('==========================================')
print('Menghitung luas dan keliling Lingkaran')
from lingkaran import *
ling = lingkaran(14)
jari = 14
keliling_ling =ling.keliling()
luas_ling=ling.luas()
print('1.LINGKARAN PERTAMA')
print('jari2nya \t\t=',jari)
print('kelilingnya \t\t=',int(keliling_ling))
print('Luasnya \t\t=',int(luas_ling))
print('###########################################')

ling2 = lingkaran(98)
jari2 = 98
keliling_ling2 =ling2.keliling()
luas_ling2=ling2.luas()
print('2.LINGKARAN KEDUA')
print('jari2nya \t\t=',jari2)
print('kelilingnya \t\t=',int(keliling_ling2))
print('Luasnya \t\t=',int(luas_ling2))

#SEGITIGASIKUSIKU
print('==========================================')
print('Menghitung luas dan keliling Segitiga Siku-siku')
from segitigasiku2 import * 

sikusiku = segitigasikusiku(15,20,25)
alas_sikusiku = 15
tinggi_sikusiku = 20
miring_sikusiku = 25
keliling_sikusiku =sikusiku.keliling()
luas_sikusiku=sikusiku.luas()
print('1.Segitiga Siku-Siku pertama')
print('Alasnya \t\t\t=',alas_sikusiku,'cm')
print('Tingginya  \t\t\t=',tinggi_sikusiku,'cm')
print('Sisi miringnya \t\t\t=',miring_sikusiku,'cm')
print('kelilingnya  \t\t\t=',keliling_sikusiku,'cm')
print('Luasnya \t\t\t=',luas_sikusiku,'cm')
print('###########################################')

sikusiku2 = segitigasikusiku(6,8,10)
alas_sikusiku2 = 6
tinggi_sikusiku2 = 8
miring_sikusiku2 = 10
keliling_sikusiku2 =sikusiku2.keliling()
luas_sikusiku2=sikusiku2.luas()
print('2.Segitiga Siku-Siku Kedua')
print('Alasnya \t\t\t=',alas_sikusiku2,'cm')
print('Tingginya  \t\t\t=',tinggi_sikusiku2,'cm')
print('Sisi miringnya \t\t\t=',miring_sikusiku2,'cm')
print('kelilingnya  \t\t\t=',keliling_sikusiku2,'cm')
print('Luasnya \t\t\t=',luas_sikusiku2,'cm')

#PersegiPanjang
print('==========================================')
print('Menghitung luas dan keliling Persegi Panjang')
from persegipanjang import *

pp = PersegiPanjang(3,4)
panjang_pp = 3
lebar_pp = 4
keliling_pp = pp.keliling()
luas_pp = pp.luas()
print('1.Persegi Panjang Pertama')
print('Panjang  =',panjang_pp)
print('Lebarnya =',lebar_pp)
print('keliling =',keliling_pp)
print('luas     =',luas_pp)
print('############################################')

pp2 = PersegiPanjang(12,25)
panjang_pp2 = 12
lebar_pp2 = 25
keliling_pp2 = pp2.keliling()
luas_pp2 = pp2.luas()
print('2.Persegi Panjang kedua')
print('Panjang   =',panjang_pp2)
print('Lebar     =',lebar_pp2)
print('keliling  =',keliling_pp2)
print('luas      =',luas_pp2)
