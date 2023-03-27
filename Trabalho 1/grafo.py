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
        if (u, v) in self.arestas or (v, u) in self.arestas:
            return True
        return False
    
    def peso(self, u, v):
        if self.haAresta(u, v):
            return self.funcao[(u, v)]
        return float('inf')
    
    def ler(self, arquivo):
        vertices = []
        arestas = []
        funcao = {}
        with open(arquivo, 'r') as f:
            for linha in f:
                linha = linha.split()
                if linha[0] == 'V':
                    vertices.append(linha[1])
                elif linha[0] == 'E':
                    arestas.append((linha[1], linha[2]))
                    funcao[(linha[1], linha[2])] = int(linha[3])
        return Grafo(vertices, arestas, funcao)