"""
Trabalho 3 - Grafos
Aluna: Brenda Silva Machado
Algoritmo de Lawler
"""

from grafo import Grafo

class Lawler:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.vertices = grafo.getVertices()
        self.arestas = grafo.getArestas()
        self.x = [0] + [float('inf')] * (2 ** len(self.vertices) - 1)
        self.S, self.index_dict = self.geraSubconjuntos()
    
    def geraSubconjuntos(self):
        S = []
        index_dict = {}  # Dicionário para mapear conjuntos aos seus índices
        for i in range(2 ** len(self.vertices)):
            subconjunto = self.geraSubconjunto(i)
            S.append(subconjunto)
            index_dict[tuple(subconjunto)] = i  # Usamos uma tupla como chave do dicionário
        return S, index_dict
    
    def geraSubconjunto(self, i):
        S = []
        for j, v in enumerate(self.vertices):
            if (i & (1 << j)) > 0:
                S.append(v)
        return S
    
    def getSComplemento(self, s):
        set_s = set(s)
        complemento = list(set(self.vertices) - set_s)
        return complemento
    
    def geraSubgrafo(self, s):
        subgrafo_vertices = []
        subgrafo_arestas = []
        
        for v in s:
            subgrafo_vertices.append(v)
            for u in self.grafo.vizinhos(v):
                if u in s:
                    subgrafo_arestas.append((v, u))
        
        return Grafo(subgrafo_vertices, subgrafo_arestas, None, None)
    
    def geraConjuntosIndependentes(self, grafo):
        conjuntos = []
        vertices = grafo.getVertices()
        arestas = grafo.getArestas()
        self.backtrack(conjuntos, vertices, arestas, 0, [])
        return conjuntos
    
    def backtrack(self, conjuntos, vertices, arestas, inicio, conjunto):
        conjuntos.append(conjunto.copy())
        for i in range(inicio, len(vertices)):
            if self.verificaIndependencia(vertices[i], conjunto):
                conjunto.append(vertices[i])
                self.backtrack(conjuntos, vertices, arestas, i + 1, conjunto)
                conjunto.pop()
    
    def verificaIndependencia(self, v, conjunto):
        for u in conjunto:
            if self.grafo.haAresta(u, v):
                return False
        return True
    
    def getComplementoConjunto(self, conjunto, s):
        complemento = s.copy()
        for v in conjunto:
            complemento.remove(v)
        return complemento
    
    def calculaColoracaoMinima(self):
        for s in self.S:
            G_linha = self.geraSubgrafo(s)
            I = self.geraConjuntosIndependentes(G_linha)
            for conjunto_I in I:
                i_complemento = self.getComplementoConjunto(conjunto_I, s)
                if i_complemento:
                    i_complemento_index = self.S.index(i_complemento)
                    s_index = self.S.index(s)
                    if self.x[i_complemento_index] != float('inf') and self.x[i_complemento_index] + 1 < self.x[s_index]:
                        self.x[s_index] = self.x[i_complemento_index] + 1

        return self.x[2 ** len(self.vertices) - 1]








