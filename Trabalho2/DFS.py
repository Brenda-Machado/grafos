"""
Trabalho 2 - Grafos
Aluna: Brenda Silva Machado
Algoritmo Auxiliar DFS
"""

from Trabalho1.grafo import Grafo

class DFS:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.visitados = [False] * grafo.qtdVertices()
        self.tempo = 0
        self.T = [0] * grafo.qtdVertices()
        self.run()
    
    def run(self):
        for i in range(self.grafo.qtdVertices()):
            if not self.visitados[i]:
                self.dfs_visit(i)
        return self.T

    def dfs_visit(self, v):
        self.visitados[v] = True
        self.tempo += 1
        for u in self.grafo.vizinhos(v):
            if not self.visitados[u]:
                self.dfs_visit(u)
        self.tempo += 1
        self.T[v] = self.tempo

