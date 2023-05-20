"""
Trabalho 2 - Grafos
Aluna: Brenda Silva Machado
Algoritmo Auxiliar DFS
"""

from grafo import Grafo

class DFS:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.visitados = []
        self.tempo_atual = 0
        self.tempos = {}
        self.fim = {}
        self.antecessores = {}
        for v in self.grafo.vertices:
            self.tempos[v] = float('inf')
            self.fim[v] = float('inf')
            self.antecessores[v] = None
    
    def componentes(self):
        for i in range(self.grafo.qtdVertices()):
            if i not in self.visitados:
                self.visit(i)
        return self.tempos, self.fim, self.antecessores

    def visit(self, v):
        self.visitados.append(v)
        self.tempo_atual += 1
        self.tempos[v] = self.tempo_atual
        for u in self.grafo.vizinhos(v):
            if u not in self.visitados:
                self.antecessores[u] = v
                self.visit(u)
        self.tempo_atual += 1
        self.fim[v] = self.tempo_atual

    def adaptado(self, fim):
        for v in fim:
            if v not in self.visitados:
                self.visit(v)
        return self.tempos, self.fim, self.antecessores


                
    




