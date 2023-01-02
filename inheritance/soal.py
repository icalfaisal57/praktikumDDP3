#parent class
class animal : 
    def __init__(self, nama, suara) :
        self.nama = nama
        self.suara = suara

    def suara(self):
        return self.suara

class cat(animal):
    pass

class dog(animal):
    pass

cat = cat("koma","meow")
print(cat.suara)