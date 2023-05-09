"""
Trabalho 2 - Grafos
Aluna: Brenda Silva Machado
Exercício 2 - Ordenação Topológica
"""

""" TO-DO
[] Arrumar a parte de OO
[] Verificar se a ordenação está sendo feita
[] Arrumar os tipos das variáveis
"""

from Trabalho1.grafo import Grafo

class ordenacaoTopologica:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.visitados = [False] * grafo.qtdVertices()
        self.tempo = 0
        self.T = [0] * grafo.qtdVertices()
        self.O = []
    
    def dfs_ordenacao(self):
        for i in range(self.grafo.qtdVertices()):
            if not self.visitados[i]:
                self.dfs_visit_ot(i)
        return self.O
    
    def dfs_visit_ot(self, v):
        self.visitados[v] = True
        self.tempo += 1
        for u in self.grafo.vizinhos(v):
            if not self.visitados[u]:
                self.dfs_visit_ot(u)
        self.tempo += 1
        self.T[v] = self.tempo
        self.O.append(v)