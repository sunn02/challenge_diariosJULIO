import sys

num_nodos = 5
aristas = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]

# distance <- initialize a matrix with infinity values
def generate_matrix(num_nodos,aristas): 
    matrix = [[0 for _ in range(num_nodos)] for _ in range(num_nodos)]
    for arista in aristas:
        i, j = arista
        matrix[i][j] = 1
        matrix[j][i] = 1
    return matrix

def min_distance(distancia, visited):
    min_distancia = sys.maxsize 
    min_nodo = -1

    for nodo in range(num_nodos):
        if distancia[nodo] < min_distancia and nodo not in visited:
            min_distancia = distancia[nodo]
            min_nodo = nodo

    return min_nodo        


def dijkstra(num_nodos, grafo, nodoPadre, nodoObjetivo):
    distancia = [sys.maxsize] * num_nodos
    distancia[nodoPadre] = 0 
    visited = set()

    for _ in range(num_nodos):
        min_nodo = min_distance(distancia, visited)
        if min_nodo == -1: #si devuelve este valor significa que ha terminado de visitar los nodos
            break
        visited.add(min_nodo)

        for nodo in range(num_nodos):
            if grafo[min_nodo][nodo] > 0 and nodo not in visited and \
                distancia[nodo] > distancia[min_nodo] + grafo[min_nodo][nodo]:
                distancia[nodo] = distancia[min_nodo] + grafo[min_nodo][nodo]
    return distancia[nodoObjetivo]

nodoPadre = 0
nodoObjetivo = 4
grafo = generate_matrix(num_nodos, aristas) 
distancia = dijkstra(num_nodos, grafo, nodoPadre, nodoObjetivo)
print(f"La distancia más corta desde el nodo {nodoPadre} al nodo {nodoObjetivo} es: {distancia}")


    