"""
Trabalho 2 - Grafos
Aluna: Brenda Silva Machado
Exercício 3 - Algoritmo de Prim para Árvores Geradoras Mínimas
"""

from grafo import Grafo
import heapq
import random

class Prim:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.antecessores = {}
        self.chave = {}
        self.fila_prioridade = []
        self.vertices_restantes = set()

    def run(self):
        u = random.choice(list(self.grafo.vertices))
        self.chave[u] = 0
        for v in self.grafo.vertices:
            self.vertices_restantes.add(v)
            if v != u:
                self.chave[v] = float('inf')
            heapq.heappush(self.fila_prioridade, (self.chave[v], u, v))

        while self.fila_prioridade:
            try:
                _, u, v = heapq.heappop(self.fila_prioridade)
            except IndexError:
                break

            if v in self.vertices_restantes:
                self.vertices_restantes.remove(v)

                for w in self.grafo.vizinhos(v):
                    if w in self.vertices_restantes:
                        peso_uv = float(self.grafo.peso(v, w))
                        if peso_uv is not None and peso_uv < self.chave[w]:
                            self.antecessores[w] = v
                            self.chave[w] = peso_uv
                            heapq.heappush(self.fila_prioridade, (self.chave[w], v, w))

        return self.antecessores
    
    def print(self):
        soma = 0
        for v in self.antecessores:
            peso = self.grafo.peso(self.antecessores[v], v)
            soma += float(peso) if peso is not None else 0

        print(f"{soma:.1f}")
        arestas = []
        for v in self.antecessores:
            arestas.append(f"{self.antecessores[v]}-{v}")
        print(", ".join(arestas))