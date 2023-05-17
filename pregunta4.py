""""
PREGUNTA 4
Nick Fury se encuentra en los cuarteles generales de S.H.I.E.L.D. y debe visitar a varios superhéroes para convencerlos de unirse para formar un grupo de vengadores, dado que es un asunto de suma importancia nos solicita implementar un algoritmo que permita determinar el recorrido de menor distancia (el menor posible, no importa que sea el óptimo) y terminar dicho recorrido de vuelta en los cuarteles (solo se puede pasar una vez por cada lugar).

    a. Considere los siguientes superhéroes: S.H.I.E.L.D.
    
    b. las distancias entre la localización de cada superhéroe están cargadas en la siguiente matriz:
"""

import itertools

distancias = [
    [0, 675, 400, 166, 809, 720, 399, 233],
    [675, 0, 540, 687, 179, 348, 199, 401],
    [400, 540, 0, 107, 752, 521, 385, 280],
    [166, 687, 107, 0, 111, 540, 990, 361],
    [809, 179, 752, 111, 0, 206, 412, 576],
    [720, 348, 521, 540, 206, 0, 155, 621],
    [399, 199, 385, 990, 412, 155, 0, 100],
    [233, 401, 280, 361, 576, 621, 100, 0]
]