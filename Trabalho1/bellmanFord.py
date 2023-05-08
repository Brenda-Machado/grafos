"""
Trabalho 1 - Grafos
Aluna: Brenda Silva Machado
Exercício 4 - Algoritmo de Bellman-Ford
"""

from grafo import Grafo

class BellmanFord:
    def __init__(self, grafo: Grafo, s):
        self.grafo = grafo
        self.s = s
        self.distancia = {}
        self.nodo = {}
        self.caminhos = {}

    def busca(self):
        # Inicializa as distâncias com infinito para todos os vértices, exceto o inicial
        for v in self.grafo.vertices:
            self.distancia[v] = float('inf')
        self.distancia[self.s] = 0

        # Relaxa todas as arestas |V|-1 vezes
        for i in range(self.grafo.qtdVertices() - 1):
            for aresta in self.grafo.arestas:
                u, v = aresta
                if self.distancia[u] + self.grafo.peso(u, v) < self.distancia[v]:
                    self.distancia[v] = self.distancia[u] + self.grafo.peso(u, v)
                    self.nodo[v] = u

        # Verifica se há ciclo negativo
        for aresta in self.grafo.arestas:
            u, v = aresta
            if self.distancia[u] + self.grafo.peso(u, v) < self.distancia[v]:
                raise ValueError("O grafo contém um ciclo negativo")

    def imprimir(self):
        self.busca()
        for v in self.grafo.vertices:
            vertice = v
            caminho = []
            distancia = self.distancia[v]
            while v != self.s:
                caminho.append(v)
                v = self.nodo[v]
            caminho.append(self.s)
            caminho.reverse()

            caminho_str = ",".join([str(u) for u in caminho])
            print(f"{vertice}: {caminho_str}; d={distancia}")



