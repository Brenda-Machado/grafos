"""
Trabalho 2 - Grafos
Aluna: Brenda Silva Machado
Exercício 2 - Ordenação Topológica
"""

from grafo import Grafo

class ordenacaoTopologica:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.visitados = []
        self.tempo = 0
        self.T = {}
        self.O = []
    
    def ordenacao(self):
        for i in range(self.grafo.qtdVertices()):
            if i not in self.visitados:
                self.visit_ot(i)
        return self.O
    
    def visit_ot(self, v):
        self.visitados.append(v)
        self.tempo += 1
        for u in self.grafo.vizinhos(v):
            if u not in self.visitados:
                self.visit_ot(u)
        self.tempo += 1
        self.T[v] = self.tempo
        self.O.append(v)
    
    def print(self):
        ordem_topologica = [str(v) for v in self.O[::-1] if v in self.grafo.vertices]
        print(" → ".join(ordem_topologica))
