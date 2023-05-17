""""
PREGUNTA 3
Kamala Khan alias Ms. Marvel es una adolescente Musulmana Pakistaní-estadounidense de Nueva Jersey. 
En el MCU tiene un linaje mutante latente activado unos misteriosos anillos que le dan una polimorfa con la capacidad de estirar su cuerpo de casi cualquier forma imaginable.
Kamala era una gran fan de los superhéroes, especialmente de Carol Danvers, la antigua Ms. Marvel y por eso se ha convertido en una experta en redes sociales,
pero nos ha pedido ayuda para implementar un grafo social y los algoritmos necesarios para atender los siguientes requerimientos:

    a. cargar superhéroes de la siguiente tabla como vértices (puntos o nodos con los que están conformado los grafos. Llamaremos grado de un vértice, al número de aristas de las que es extremo) del grafo;
    
    b. cargar estos superhéroes con las siguientes etiquetas: Twitter, Instagram respectivamente, que representan si la persona del vértice origen sigue o es amigo de la persona del vértice destino;
    
    c. hallar el árbol de expansión máximo para cada red social (considere el grafo como no dirigido para este punto), es decir que las conexiones deben ser las de mayor peso (ósea el que tenga mayor interacción);
       para lo cual, si desea utilizar Prim o Kruskal sin modificar el código, puede determinar la arista (relación entre dos vértices de un grafo) de mayor peso y cuando aplique este algoritmo, debe que considerar el peso de cada arista será la arista de mayor peso menos el peso de la arista;
    
    d. determine si es posible conectar la persona Capitana Marvel con Nick Fury a través de la red social Twitter;
    
    e. determine si es posible conectar la persona The Winter Soldier con Iron Man a través de cualquier red social;
    
    f. indique a todas las personas que sigue a través de su red de Instagram Thor.
"""

# ---------------------------------------
# Apartado A: Carga de los datos
# ---------------------------------------

superheroes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']

twitter_matrix = [
    [0, 75, 40, 16, 80, 20, 99, 23],
    [75, 0, 50, 67, 79, 38, 99, 41],
    [40, 50, 0, 17, 75, 52, 85, 28],
    [16, 67, 17, 0, 11, 50, 90, 36],
    [80, 79, 75, 11, 0, 26, 12, 56],
    [20, 38, 52, 50, 26, 0, 55, 61],
    [99, 99, 85, 90, 12, 55, 0, 10],
    [23, 41, 28, 36, 56, 61, 10, 0]
]

instagram_matrix = [
    [0, 61, 44, 66, 56, 74, 11, 65],
    [12, 0, 47, 41, 12, 38, 99, 41],
    [41, 23, 0, 45, 12, 89, 42, 14],
    [12, 69, 11, 0, 12, 50, 78, 63],
    [89, 19, 72, 11, 0, 26, 12, 56],
    [72, 34, 21, 65, 12, 0, 78, 41],
    [12, 87, 35, 99, 42, 15, 0, 10],
    [33, 41, 24, 61, 45, 41, 11, 0]
]

# ---------------------------------------
# Apartado B: Creación de los grafos
# ---------------------------------------

def create_graph(superheroes, matrix):
    graph = {}
    for i in range(len(superheroes)):
        for j in range(i + 1, len(superheroes)):
            hero1 = superheroes[i]
            hero2 = superheroes[j]
            weight = matrix[i][j]
            if hero1 in graph:
                graph[hero1][hero2] = weight
            else:
                graph[hero1] = {hero2: weight}
            if hero2 in graph:
                graph[hero2][hero1] = weight
            else:
                graph[hero2] = {hero1: weight}
    return graph

twitter_graph = create_graph(superheroes, twitter_matrix)
instagram_graph = create_graph(superheroes, instagram_matrix)

# ---------------------------------------
# Apartado C: Árbol de expansión máximo
# ---------------------------------------

def maximum_spanning_tree(graph):
    max_tree = {}
    visited = set()
    start = None
    for node in graph:
        if start is None or max(graph[node].values()) > max(graph[start].values()):
            start = node
    visited.add(start)
    while len(visited) < len(graph):
        max_edge = None
        for node in visited:
            for neighbor in graph[node]:
                if neighbor not in visited and (max_edge is None or graph[node][neighbor] > graph[max_edge[0]][max_edge[1]]):
                    max_edge = (node, neighbor)
        if max_edge is not None:
            max_tree[max_edge[0]] = {max_edge[1]: graph[max_edge[0]][max_edge[1]]}
            max_tree[max_edge[1]] = {max_edge[0]: graph[max_edge[0]][max_edge[1]]}
            visited.add(max_edge[1])
    return max_tree

max_tree_twitter = maximum_spanning_tree(twitter_graph)
max_tree_instagram = maximum_spanning_tree(instagram_graph)

# ---------------------------------------
# Apartado D: Conexión entre 'Captain America' y 'Nick Fury' en Twitter
# ---------------------------------------

def has_path(graph, start, end):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        visited.add(node)
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False

has_path_twitter = has_path(twitter_graph, 'Captain America', 'Nick Fury')

# ---------------------------------------
# Apartado E: Conexión entre 'The Winter Soldier' e 'Iron Man' en cualquier red social
# ---------------------------------------

has_path_social = has_path(twitter_graph, 'The Winter Soldier', 'Iron Man') or has_path(instagram_graph, 'The Winter Soldier', 'Iron Man')

# ---------------------------------------
# Apartado F: Personas que Thor sigue en Instagram
# ---------------------------------------

thor_follows = [neighbor for neighbor in instagram_graph['Thor']]

if __name__ == '__main__':

    print("\n")
    print(f"Árbol de expansión máximo para Twitter: {max_tree_twitter}") 
    print("\n")
    print(f"Árbol de expansión máximo para Instagram: {max_tree_instagram}")
    print("\n")
    print(f"¿Es posible conectar a Captain America con Nick Fury en Twitter?: {'Sí' if has_path_twitter else 'No'}")
    print("\n")
    print(f"¿Es posible conectar a The Winter Soldier con Iron Man en alguna red social?: {'Sí' if has_path_social else 'No'}")
    print("\n")
    print(f"Thor sigue a las siguientes personas en Instagram: {thor_follows}")
    print("\n")
