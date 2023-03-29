"""
Trabalho 1 - Grafos
Aluna: Brenda Silva Machado
Exercício 2 - Busca em Largura
"""

from grafo import Grafo

class BuscaLargura:
    def __init__(self, grafo, s):
        self.grafo = grafo
        self.s = s
        self.distancia = {}
        self.nodo = {}
        self.fila = []
        self.visitados = []
    
    def busca(self):
        self.distancia[self.s] = 0
        self.nodo[self.s] = None
        self.fila.append(self.s)
        while self.fila.empty() == False:
            u = self.fila.pop(0)
            self.visitados.append(u)
            for v in self.grafo.vizinhos(u):
                if v not in self.visitados:
                    self.distancia[v] = self.distancia[u] + 1
                    self.nodo[v] = u
                    self.fila.append(v)
        return self.distancia, self.nodo
    
