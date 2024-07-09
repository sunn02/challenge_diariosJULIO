grafo = { 
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : [],
  '2' : [],
  '4' : [],
}
visited = []
queue = []

def bfs(visited, grafo, nodo):
    visited.append(nodo)
    queue.append(nodo)
    
    while queue:
        cabeza = queue.pop(0)
        for vecino in grafo[cabeza]:
            if vecino not in visited:
                visited.append(vecino)
                queue.append(vecino)
    
bfs(visited, grafo, "5")
print(visited)
    
# Pseucode
# create a queue Q 
# mark v as visited and put v into Q 
# while Q is non-empty 
#     remove the head u of Q 
#     mark and enqueue all (unvisited) neighbours of u