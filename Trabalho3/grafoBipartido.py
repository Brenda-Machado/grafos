"""
Trabalho 3 - Grafos
Aluna: Brenda Silva Machado
Representação de Grafo Bipartido
"""

class grafoBipartido:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas
    
    def getVertices(self):
        return self.vertices

    def getArestas(self):
        return self.arestas
    
    def qtdVertices(self):
        return len(self.vertices)
    
    def qtdArestas(self):
        return len(self.arestas)
    
    def grau(self, v):
        return len(self.vizinhos(v))
    
    def rotulo(self, v):
        return self.vertices[v]

    def vizinhos(self, v):
        vizinhos = []
        if self.arestas:
            for aresta in self.arestas:
                if v in aresta:
                    vizinhos.append(aresta[0] if aresta[0] != v else aresta[1])
        else:
            for arco in self.arcos:
                if v == arco[0]:
                    vizinhos.append(arco[1])
        return vizinhos
    
    def haAresta(self, u, v):
        return set((u, v)) in map(set, self.arestas)
    
    def ler(self, arquivo):
        with open(arquivo, "r") as f:
            header = f.readline().split()
            num_vertices = int(header[1])

            vertices = {}
            for i in range(num_vertices):
                line = f.readline().split()
                vertices[int(line[0])] = line[1]

            arestas = []
            line = f.readline().split()
            while line and line[0] == "*edges":
                line = f.readline().split()
                while line:
                    aresta = (int(line[0]), int(line[1]))
                    arestas.append(aresta)
                    line = f.readline().split()
            return grafoBipartido(vertices, arestas)
