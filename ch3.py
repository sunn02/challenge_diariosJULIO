grafo = { #Se utiliza diccionario para simular una adjacency list para representar el grafo
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : [],
  '2' : [],
  '4' : [],
}

visited = set() #Almacena los nodos visitados

def dfs(visited, grafo, nodo):
    if nodo not in visited:
        print(nodo)
        visited.add(nodo)
        for vecino in grafo[nodo]:
            dfs(visited, grafo, vecino)
dfs(visited, grafo, "5")
            