

class Motor():
    def __init__(self, tipo):
        self.tipo = tipo
        
    def describir_motor(self):
        print(f'Motor de tipo: {self.tipo}')
        
class Auto():
    def __init__(self, tipo_motor):
        self.motor = Motor(tipo_motor) # # Crea una instancia de Motor
    
    def describir_motor(self):
        self.motor.describir_motor() # # Llama al método describir_motor de la instancia de Motor
        
        
auto1 = Auto("zz")
auto1.describir_motor()
auto2 = Auto("idk")
auto2.describir_motor()