nilai = {"firda":90,"anyong":80,"ica":99,"ison":78}
print("data nilai :",nilai)
print("\n------------cetak value saja-------------")
for skor in nilai.values():
    print("data nilai:",skor)
print("\n----------cetak key saja-----")
for nama in nilai.keys():
    print("data siswa:",nama)
print("\n----------cetak key dan value bareng----")
for nama,skor in nilai.items():
    print("nama siswa : %s \t Nilai : %i" % (nama,skor))