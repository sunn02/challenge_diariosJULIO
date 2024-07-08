def busqueda():
    valor_min = 0
    valor_max = len(num_primos) - 1
    

    while valor_max <= valor_min:
        valor_adivinado = (valor_max + valor_min)//2
        if valor_adivinado == objetivo:
            return valor_adivinado
        elif valor_adivinado < objetivo:
            valor_min = valor_adivinado + 1
        elif valor_adivinado > objetivo:
            valor_max = valor_adivinado - 1 
    return -1

num_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
objetivo = 37
resultado = busqueda()
if resultado != -1:
    print(f'{objetivo} está en la lista, en el índice {resultado}')
else:
    print(f'El objetivo {objetivo} no está en la lista')


# Pseucodigo
# Sea min = 0 y max = n-1.
# Si max < min, entonces detente: target no está en array. Regresa -1.
# Calcula guess como el promedio de max y min, redondeado hacia abajo (para que sea un entero).
# Si array[guess] es igual a target, entonces detente. ¡Lo encontraste! Regresa guess.
# Si el intento fue demasiado bajo, es decir, array[guess] < target, entonces haz min = guess + 1.
# De lo contrario, el intento fue demasiado alto. Haz max = guess - 1.
# Regresa al paso 2.
