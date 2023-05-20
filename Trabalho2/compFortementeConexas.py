"""
Trabalho 2 - Grafos
Aluna: Brenda Silva Machado
Exercício 1 - Representação de Componentes Fortemente Conexas
"""

from grafo import Grafo
from DFS import DFS

class compFortementeConexas:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.dfs = DFS(self.grafo)
        self.antecessores = [None] * grafo.qtdVertices()
        self.fim = [float('inf')] * grafo.qtdVertices()
        self.tempos = [float('inf')] * grafo.qtdVertices()
        self.grafo_t = grafo.transposto()
        self.dfs_t = DFS(self.grafo_t)
        self.antecessores_t = [None] * grafo.qtdVertices()

    def run(self):
        tempos, fim, antecessores = self.dfs.componentes()
        self.tempos = tempos
        self.fim = fim
        self.antecessores = antecessores

        tempos_t, fim_t, antecessores_t = self.dfs_t.componentes()
        self.antecessores_t = antecessores_t

    def print(self):
        componentes = []
        visitados = []

        for v in self.grafo.vertices:
            if v not in visitados:
                componente = []
                self.map_comp(v, visitados, componente)
                componentes.append(componente)

        for componente in componentes:
            print("{" + ", ".join(str(v) for v in componente) + "}")

    def map_comp(self, v, visitados, componente):
        visitados.append(v)
        componente.append(v)

        for vizinho in self.grafo_t.vizinhos(v):
            if vizinho not in visitados:
                self.map_comp(vizinho, visitados, componente)

    def get_antecessores(self):
        return [self.antecessores[v] + 1 if self.antecessores[v] is not None else None for v in range(self.grafo.qtdVertices())]
