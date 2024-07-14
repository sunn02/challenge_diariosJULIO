#Operaciones elementales sobre Pilas y Colas
# Insertar: Push -> apilar (Pila), Enqueue -> encolar (Cola)
# Eliminar: Pop -> desapilar (Pila), Dequeue -> desencolar (Cola)

#(Pila)"last-in, first-out”, que dicta que el primer elemento que fue añadido a la pila 
# será el último en ser removido de la misma.
#(Cola)“first-in, first-out”, que dicta que el primer elemento que fue añadido a la cola 
# será el primero en ser removido.

pila = ["Manzana", "Banana", "Pera", "Naranja", "Sandia"]
print(f'La antigua pila de elementos es: {pila}')
pila.append("Frutilla")
print(f'La pila con el elemento agregado es: {pila}')

print(f'El ultimo elemento agregado en la lista se elimina ({pila.pop()}) y queda asi:{pila}')

cola = ["Manzana", "Banana", "Pera", "Naranja", "Sandia"]
print(f'La antigua cola de elementos es: {cola}')
cola.append("Frutilla")
print(f'La cola con el elemento agregado es: {cola}')

print(f'El primer elemento agregado en la lista se elimina ({cola.pop(0)}) y queda asi:{cola}')
