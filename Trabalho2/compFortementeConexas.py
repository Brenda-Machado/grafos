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
        tempos_t, fim_t, antecessores_t = self.dfs_t.adaptado(self.fim)
        self.antecessores_t = antecessores_t

    def print(self):
        pass


    

    