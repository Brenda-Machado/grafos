"""
Trabalho 1 - Grafos
Aluna: Brenda Silva Machado
Exercício 3 - Ciclo Euleriano
"""

class CicloEuleriano:
    def __init__(self, grafo):
        self.grafo = grafo
        self.ciclo = []
        self.visitados = []

    def busca(self):
        for v in self.grafo.vertices:
            if self.grau(v) % 2 != 0:
                return False
        if next(iter(self.grafo.vertices)) not in self.visitados:
            v = next(iter(self.grafo.vertices))
            self.visitados.append(v)

        while len(self.visitados) < self.grafo.qtdVertices():
            w = None
            for u in self.grafo.vizinhos(v):
                if u not in self.visitados:
                    w = u
                    break
            
            if w is None:
                break
            self.visitados.append(w)
            self.ciclo.append((v, w))
            v = w

        self.ciclo.append((v, next(iter(self.visitados))))

        return True

    def grau(self, v):
        return len(self.grafo.vizinhos(v))

    def imprimir(self):
        if self.busca():
            print(1)
            vertices = list(set([v for aresta in self.ciclo for v in aresta]))
            vertices.append(vertices[0])
            ciclo = ','.join(str(v) for v in vertices)
            print(ciclo)
        else:
            print(0)


