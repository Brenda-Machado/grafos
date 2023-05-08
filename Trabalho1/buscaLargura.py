"""
Trabalho 1 - Grafos
Aluna: Brenda Silva Machado
Exercício 2 - Busca em Largura
"""

from grafo import Grafo

class BuscaLargura:
    def __init__(self, grafo : Grafo, s):
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
        self.visitados.append(self.s)
        nivel_atual = 0
        vertices_no_nivel = [self.s]
        while self.fila:
            u = self.fila.pop(0)
            nivel_vizinho = self.distancia[u] + 1
            for v in self.grafo.vizinhos(u):
                if v not in self.visitados:
                    self.visitados.append(v)
                    self.distancia[v] = nivel_vizinho
                    self.nodo[v] = u
                    self.fila.append(v)
            if nivel_vizinho > nivel_atual:
                print(nivel_atual, ':', vertices_no_nivel)
                nivel_atual = nivel_vizinho
                vertices_no_nivel = [v for v in self.visitados if self.distancia[v] == nivel_atual]
            else:
                vertices_no_nivel = [v for v in self.visitados if self.distancia[v] == nivel_atual]

        print(nivel_atual, ':', vertices_no_nivel)
    
