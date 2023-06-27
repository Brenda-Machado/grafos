"""
Trabalho 3 - Grafos
Aluna: Brenda Silva Machado
Algoritmo de Hopcroft-Karp
"""

from grafoBipartido import grafoBipartido
from collections import deque

class hopcroftKarp():
    def __init__(self, grafo: grafoBipartido):
        self.grafo = grafo
        self.vertices = grafo.getVertices()
        self.arestas = grafo.getArestas()
        self.distancias = self.mapeiaDistancias()
        self.mate = self.mapeiaMate()
        self.X = self.mapeiaX()
        self.Y = self.mapeiaY()
        self.max_matching = self.calcularMaxMatching() # Emparelhamento máximo

    def mapeiaX(self):
        x = set()
        for aresta in self.arestas:
            x.add(aresta[0])
        return x

    def mapeiaY(self):
        y = set()
        for aresta in self.arestas:
            y.add(aresta[1])
        return y

    def mapeiaMate(self):
        mate = {}
        for v in self.vertices:
            mate[v] = None
        return mate

    def mapeiaDistancias(self):
        distancias = {}
        for v in self.vertices:
            distancias[v] = None
        return distancias

    def getMatching(self):
        return self.max_matching

    def getMate(self):
        return self.mate

    def calcularMaxMatching(self):
        print(self.X)
        print(self.Y)
        max_matching = 0
        while self.bfs():
            for x in self.X:
                if self.mate[x] is None:
                    if self.dfs(x):
                        max_matching += 1
        return max_matching

    def bfs(self):
        q = deque()
        for x in self.X:
            if self.mate[x] is None:
                self.distancias[x] = 0
                q.append(x)
            else:
                self.distancias[x] = float('inf')
        self.distancias['null'] = float('inf')
        while q:
            x = q.popleft()
            print(self.distancias)
            if self.distancias[x] < self.distancias['null']:
                for y in self.grafo.vizinhos(x):
                    if self.mate[y] is not None and self.distancias[self.mate[y]] == float('inf'):
                        self.distancias[self.mate[y]] = self.distancias[x] + 1
                        q.append(self.mate[y])
        return self.distancias['null'] != float('inf')

    def dfs(self, x):
        if x is not None:
            for y in self.grafo.vizinhos(x):
                if self.distancias[self.mate[y]] == self.distancias[x] + 1:
                    if self.dfs(self.mate[y]):
                        self.mate[y] = x
                        self.mate[x] = y
                        return True
            self.distancias[x] = float('inf')
            return False
        return True