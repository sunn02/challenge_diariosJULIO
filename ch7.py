#Implementing an Algorithm for Priority Queue
# The steps involved in implementing a Priority Queue algorithm are as follows:

# 1	Create an empty queue
# 2	Add elements to the queue, simultaneously applying the priority function to assign a priority to each element
# 3	Use a dequeue operation to remove the highest priority element when ready
# 4	Continue dequeuing until the queue is empty

# import heapq
# #The first step is to set up a list of elements. 
# # Each element in this list is a tuple where the first value is the priority 
# # and the second value is the item you want to add to the Priority Queue:
# queue = [(3, 'apple'), (2, 'banana'), (1, 'cherry')]
# heapq.heapify(queue)
# print(queue)
# print(heapq.heappop(queue)) #This will always remove and return the smallest element from the Priority Queue.


queue = []

def agregar(elemento, prioridad):
    queue.append((prioridad, elemento))
    queue.sort() #Organiza la lista por orden de prioridad
    
def eliminar():
    if not queue: #retorna None si la lista esta vacia
        return None
    return queue.pop(0) #Elimina el elemento con la prioridad mas pequeña, asi considerando que sea de mayor prioridad


agregar('manzana', 3)
agregar('banana', 2)
agregar('pera', 1)
agregar('frutilla', 5)
agregar('kiwi', 4)
print(queue)

while queue: #itera la lista hasta que este vacia
    elemento_eliminado = eliminar()
    if elemento_eliminado is not None:
        print(f'Elemento eliminado:{elemento_eliminado[1]},Prioridad: {elemento_eliminado[0]}')
    
print(queue)
    