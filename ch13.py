
class CuentaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo
        
    def depositar_saldo(self):
        self.saldo_depositado = int(input("Ingrese un monto:"))
        self.saldo += self.saldo_depositado
        
    def consultar_saldo(self):
        print(f"Saldo actual:{self.saldo}")
    
cuenta = CuentaBancaria(10000)

cuenta.consultar_saldo()
cuenta.depositar_saldo()
cuenta.consultar_saldo()