# Search methods
"""Searches - Grupo 43 - Gabriel Dominguez Torres y Meng Fei Dai

Ejecutamos el programa printeando las 4 funciones (BFS (anchura), DFS (en profundidad),
Branch and Bound (ramificacion y acotación) y el Branch And Bound con heuristica.) creada en
el search.py para comprobar de forma visual cuál es la estrategia más optima. El programa
muestra un recuento de los nodos visitados y expandidos en cada iteración con cada estrategia.
Comprobando en su última iteración cuál de las estrategia es más óptimo. En este caso la
mejor estrategia sería el Branch And Bound con heuristica."""

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_graph_search(ab).path())
print(search.branch_and_bound_heuristic_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
