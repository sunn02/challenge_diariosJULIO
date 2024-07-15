# Define una clase base FormaGeometrica con métodos calcular_area y calcular_perimetro. 
# Crea clases derivadas Rectangulo y Circulo que sobrescriban estos métodos.
import math 

class FormaGeometrica():
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    
class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def calcular_area(self):
        area = self.ancho * self.alto
        print(f"El area del rectangulo es:{area}")
    def calcular_perimetro(self):
        perimetro = 2 * (self.ancho + self.alto)
        print(f"El perimetro del rectangulo es:{perimetro}")

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        print(f"El area del circulo es:{area}")
    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print(f"El perimetro del circulo es:{perimetro}")
        
rectangulo1 = Rectangulo(5, 10)
rectangulo1.calcular_area()

circulo1 = Circulo(3)
circulo1.calcular_perimetro()