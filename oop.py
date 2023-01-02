#object oriented programming
#merupaka suatu konsep pemisahan antara suatu class yang akan dicetak dalam bentuk objek
#ada 2 hal penting pertama adalah class 
#class adalah suatu cetakan atau design suatu blueprint yang didalam nya ada atribut dan method
#yang jedua adalah objek, objek adalah hasil dari penerapan class yang sudah di buat
#1class dapat mencipatakan banyak objek.
#membuat class di python menggunakan kata kunci class

class mahasiswa:
    #atribut dan variabel tanpa konstruktor
    # nim = ""
    # nama = ""
    # rombel = ""

    #fungsi konstruktor
    def __init__(self, nama, nim, rombel) :
        self.nama = nama
        self.nim = nim
        self.rombel = rombel

    def cetak(self):
        print(self.nim)
        print(self.nama)
        print(self.rombel)
    #method / fungsi
    def lulus(self, nilai):
        if(nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")
# tanpa menggunakan fungi konstruktor
# mhs1 = mahasiswa()
# mhs1.nama = "ahmad faisal nurhakim"
# mhs1.nim = "0110222232"
# mhs1.rombel = "ti14"
# print(mhs1.nama)
# print(mhs1.nim)
# print(mhs1.rombel)
# mhs1.lulus(95)

# mhs2 = mahasiswa()
# mhs2.nama = "andi"
# mhs2.nim = "011012345"
# mhs2.rombel = "ti10"
# print(mhs2.nama)
# print(mhs2.nim)
# print(mhs2.rombel)
# mhs2.lulus(90)

#print objek dengan kosntruktor
mahasiswa1 = mahasiswa("ahmad faisal nurhakim", "0110222232", "ti14")
mahasiswa1.cetak()
mahasiswa1.lulus(99)