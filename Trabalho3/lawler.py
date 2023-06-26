"""
Trabalho 3 - Grafos
Aluna: Brenda Silva Machado
Algoritmo de Lawler
"""

from grafo import Grafo
import numpy as np

class Lawler:
    def __init__(self, grafo : Grafo):
        self.grafo = grafo
        self.vertices = grafo.getVertices()
        self.arestas = grafo.getArestas()
        # x = vetor indexado entre 0 e 2^|V| − 1
        self.x = np.arange(2**(len(self.vertices)))
        self.x[0] = 0
        self.S = self.geraSubconjuntos()
    
    def geraSubconjuntos(self):
        S = []
        for i in range(2**(len(self.vertices))):
            S.append(self.geraSubconjuntos(i))
        return S
    
