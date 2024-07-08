lista = [1, 4 , 3, 2, 5]

# 1
# 4
# 3
# 2
# 5

def seleccion():

    print(f'La lista sin ordenar es:{lista}')
    
    largo = len(lista)
    for i in range(largo): #Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        for j in range(i+1, largo):
            if lista[minimo] > lista[j]:
                minimo = j

        lista[i], lista[minimo]     = lista[minimo], lista[i] # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
    # Repetimos el proceso hasta terminar
    print(f'La lista ordenada es:{lista}')

seleccion()



