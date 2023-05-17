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