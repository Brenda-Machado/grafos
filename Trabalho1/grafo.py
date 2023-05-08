"""
Trabalho 1 - Grafos
Aluna: Brenda Silva Machado
Exercício 1 - Representação de grafos
"""

class Grafo:
    def __init__(self, vertices, arestas, funcao):
        self.vertices = vertices
        self.arestas = arestas 
        self.funcao = funcao 
    
    def qtdVertices(self):
        return len(self.vertices)
    
    def qtdArestas(self):
        return len(self.arestas)
    
    def grau(self, v):
        return len(self.vizinhos(v))
    
    def rotulo(self, v):
        return v
    
    def vizinhos(self, v):
        vizinhos = []
        for aresta in self.arestas:
            if v in aresta:
                vizinhos.append(aresta[0] if aresta[0] != v else aresta[1])
        return vizinhos
    
    def haAresta(self, u, v):
        return set((u, v)) in map(set, self.arestas)

    
    def peso(self, u, v):
        if self.haAresta(u, v):
            return self.funcao.get((u, v), float('inf'))
        return float('inf')

    
    def ler(self, arquivo):
        with open(arquivo, "r") as f:

            header = f.readline().split()
            num_vertices = int(header[1])
            
            vertices = {}
            for i in range(num_vertices):
                line = f.readline().split()
                vertices[int(line[0])] = line[1]
            
            arestas = []
            funcao = {}
            line = f.readline().split()
            while line and line[0] == "*edges":
                line = f.readline().split()
                while line:
                    aresta = (int(line[0]), int(line[1]))
                    arestas.append(aresta)
                    w = float(line[2])
                    funcao[aresta] = w
                    line = f.readline().split()
            
            return Grafo(vertices, arestas, funcao)
    
    """TO-DO
    Testar isso aqui
    """
    def transposto(self):
        arestas = [(v, u) for (u, v) in self.arestas]
        return Grafo(self.vertices, arestas, self.funcao)
    