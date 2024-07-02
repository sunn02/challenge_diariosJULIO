def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return True
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False


lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
objetivo = 7

resultado = busqueda_binaria(lista_ordenada, objetivo)

print(f"El número {objetivo} {'está' if resultado else 'no está'} en la lista.")