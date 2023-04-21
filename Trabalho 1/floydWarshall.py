"""
Trabalho 1 - Grafos
Aluna: Brenda Silva Machado
Exercício 5 - Algoritmo de Floyd-Warshall
"""

class FloydWarshall:
    def __init__(self, grafo):
        self.grafo = grafo
        self.distancia = [[float("inf") for _ in range(grafo.qtdVertices())] for _ in range(grafo.qtdVertices())]
        self.nodo = [[None for _ in range(grafo.qtdVertices())] for _ in range(grafo.qtdVertices())]
    
    def buscarMenorCaminho(self):
        n = self.grafo.qtdVertices()
        for i in range(n):
            for j in range(n):
                if self.grafo.haAresta(i, j):
                    self.distancia[i][j] = self.grafo.peso(i, j)
                    self.nodo[i][j] = i
                    # atualiza a distância para o vértice 1
                    if i == 0:
                        self.distancia[0][j] = self.grafo.peso(0, j)
                        self.nodo[0][j] = 0
                elif i == j:
                    self.distancia[i][j] = 0
                else:
                    self.distancia[i][j] = float("inf")
                    self.nodo[i][j] = None

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.distancia[i][j] > self.distancia[i][k] + self.distancia[k][j]:
                        self.distancia[i][j] = self.distancia[i][k] + self.distancia[k][j]
                        self.nodo[i][j] = self.nodo[k][j]
    
    def imprimir(self):
        for i in range(self.grafo.qtdVertices()):
            caminho = []
            for j in range(self.grafo.qtdVertices()):
                if self.distancia[i][j] == float('inf') or self.distancia[i][j] == None:
                    caminho.append(str(self.distancia[i][j]))
                else:
                    caminho.append(str(int(self.distancia[i][j])))

            print(f"{i+1}:{','.join(caminho)}")
