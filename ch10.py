

# lista = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57]

# lista_unicos = []

# for i in lista:
#     if i not in lista_unicos:
#         lista_unicos.append(i)
# print(lista_unicos)

def eliminar_duplicado(lista):
    lista_unicos = []
    
    for i in lista:
        if i not in lista_unicos:
            lista_unicos.append(i)
    print(lista_unicos)
            
eliminar_duplicado(lista=[2, 7, 58, 7, 45, 26, 10, 8, 58, 57])
