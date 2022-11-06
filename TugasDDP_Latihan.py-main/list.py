buah = ["mangga","alpukat","jambu","pisang","melon","leci"]
buah [2] = "jeruk"
print(buah)
buah.append("duren")
print(buah)

#listmakanan
listmakanan = [
    ["bakwan","combro","tempe","gehu"],
    ["sop ceker","sop iga","sop buntut"],
    ["nasi uduk","nasi putih","nasgor"]
]
print("========cetak per item=====")
print(listmakanan[0][0])
print(listmakanan[1][2])
print(listmakanan[2][2])
print("===cetak semuanya dgn nested loop====")
for menu in listmakanan:
    for makanan in menu:
        print(makanan)
