from grafo import Grafo
from buscaLargura import BuscaLargura
from cicloEuleriano import CicloEuleriano
from bellmanFord import BellmanFord
from floydWarshall import FloydWarshall

grafo = Grafo(None, None, None)
grafo = grafo.ler('/home/brenda/grafos/Trabalho 1/teste.txt')
# busca = BuscaLargura(grafo, 1)
# busca.busca()
# ciclo = CicloEuleriano(grafo)
# ciclo.imprimir()
# bellman = BellmanFord(grafo, 1)
# bellman.imprimir()
floyd = FloydWarshall(grafo)
floyd.buscarMenorCaminho()
floyd.imprimir()
