
class Figura():
    def imprimir(self):
        print("Imprimo una figura")

class Circulo(Figura):
    def imprimir(self):
        print("Imprimo un circulo")
        
figura = Figura()
circulo = Circulo()

figura.imprimir()
circulo.imprimir()