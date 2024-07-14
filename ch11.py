

class Punto2D():
    def __init__(self, x, y):
        self.coordenada_x = x
        self.coordenada_y = y
        
    def imprimir(self):
        print(f'Coordenadas: {self.coordenada_x, self.coordenada_y}')
        
punto = Punto2D(0,1)

punto.imprimir()
