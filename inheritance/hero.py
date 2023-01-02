#membuat class parent
class hero:
    def __init__(self, name,health) :
        self.name = name
        self.health = health

    def sayhello (self):
        print("hello", self.name)

class herostrength(hero):
    def __init__(self, name, health, strenght):
        super().__init__(name, health)
        self.strenght = strenght 

#membuat objek
mars = herostrength("mars", 95,70)
print(mars.__dict__)
mars.sayhello()