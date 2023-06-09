""""
PREGUNTA 5
Dado un grafo no dirigido con personajes del MCU de la siguiente tabla:
Implementar los algoritmos necesarios para resolver las siguientes tareas:

    a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
    
    b. hallar el árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier;
    
    c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número
    
    d. cargue todos los personajes de la tabla anterior
    
    e. indicar qué personajes aparecieron en nueve episodios de la saga.
"""

import numpy as np
from heapq import heappop, heappush


# a)

grafo = np.array([              # Matriz de adyacencia
  [0, 6, 0, 1, 8, 7, 3, 2],
  [6, 0, 0, 6, 1, 8, 9, 1],
  [0, 0, 0, 1, 2, 1, 5, 0],
  [1, 6, 1, 0, 1, 5, 9, 3],
  [8, 1, 2, 1, 0, 2, 4, 5],
  [7, 8, 1, 5, 2, 0, 1, 6],
  [3, 9, 5, 9, 4, 1, 0, 1],
  [2, 1, 0, 3, 5, 6, 1, 0]
]) 

superheroes = ["Iron Man", "Thor", "The Winter Soldier", "Captain America", "Hulk", "Black Widow", "Hawkeye", "Nick Fury"]


def algoritmo(grafo, inicio): 
    n = len(grafo) 
    visitados = [False]*n 
    pesos = [-1]*n 
    previos = [None]*n 
    pesos[inicio] = 0 
    cola_prioridad = [(0, inicio)] 

    while cola_prioridad: 
        peso, u = heappop(cola_prioridad) 
        if not visitados[u]: 
            visitados[u] = True 
            for v, peso_uv in enumerate(grafo[u]): 
                if not visitados[v] and (pesos[v] == -1 or pesos[v] < peso_uv): 
                    pesos[v] = peso_uv 
                    previos[v] = u 
                    heappush(cola_prioridad, (peso_uv, v))
    return previos 

# b)

inicio = superheroes.index("Iron Man")
previos = algoritmo(grafo, inicio)
print("Árbol de expansión máximo desde Iron Man")
for i, p in enumerate(previos):
    if p is not None:
        print(f'{superheroes[p]} -- {superheroes[i]}')

# c)

max_episodios = np.max(grafo)
print(f'\nEl número máximo de episodios que comparten dos personajes es {max_episodios}')
print('Los pares de personajes que coinciden con dicho número son:')
indices = np.where(grafo == max_episodios)
for i in range(len(indices[0])):
    if indices[0][i] != indices[1][i]:
        print(f'{superheroes[indices[0][i]]} -- {superheroes[indices[1][i]]}')

# d)

print('\nPersonajes de la tabla:')
for personaje in superheroes:
    print(personaje)

# e)

print('\nPersonajes que aparecieron en 9 episodios:')
indices_9 = np.where(grafo == 9)
for i in range(len(indices_9[0])):
    if indices_9[0][i] != indices_9[1][i]:
        print(f'{superheroes[indices_9[0][i]]} -- {superheroes[indices_9[1][i]]}')
