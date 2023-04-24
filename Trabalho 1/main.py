from grafo import Grafo
from buscaLargura import BuscaLargura
from cicloEuleriano import CicloEuleriano
from bellmanFord import BellmanFord
from floydWarshall import FloydWarshall

grafo = Grafo()
grafo = grafo.ler('teste.txt')

# Teste Busca em Largura
# busca = BuscaLargura(grafo, 1)
# busca.busca()

# Teste Ciclo Euleriano
# ciclo = CicloEuleriano(grafo)
# ciclo.imprimir()

# Teste Bellman-Ford 
# bellman = BellmanFord(grafo, 1)
# bellman.imprimir()

# Teste Floyd-Warshall
# floyd = FloydWarshall(grafo)
# floyd.buscarMenorCaminho()
# floyd.imprimir()
