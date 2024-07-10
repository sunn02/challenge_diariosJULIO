

class Nodo():
    def __init__(self, valor): #Atributos
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        
def insert(nodo,valor):
    if nodo is None: #Si el arbol esta vacio retorna ese nodo
        return Nodo(valor)
        
    if valor < nodo.valor: #Si el valor a insertar es menor que su nodo Padre, se agrega a la izquierda
        nodo.izquierda = insert(nodo.izquierda, valor) 
    if valor > nodo.valor: #Si el valor a insertar es mayor que su nodo Padre, se agrega a la derecha
        nodo.derecha = insert(nodo.derecha, valor) 
    return nodo

def inorder(nodo): #Este tipo de recorrido visita los nodos del árbol en un orden ascendente, de menor a mayor valor.
    if nodo:
        inorder(nodo.izquierda)  # Recorre el subárbol izquierdo
        print(nodo.valor)  # Visita el nodo actual
        inorder(nodo.derecha) #Recorre el subárbol izquierdo
        
if __name__ == '__main__':
 
    # 50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80
 
    r = Nodo(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
 
    inorder(r)
