
def hacer_sonido(animal):
    animal.hacer_sonido()

class Animal():
    def hacer_sonido(self):
        print("Cada animal realiza un sonido distinto")
    
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

perro = Perro()
hacer_sonido(perro)

