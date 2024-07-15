
class Animal():
    def hacer_sonido(self):
        print("Cada animal realiza un sonido distinto")
    
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

animal = Animal()
perro = Perro()

animal.hacer_sonido()
perro.hacer_sonido()    
