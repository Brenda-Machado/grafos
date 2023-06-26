"""
Trabalho 3 - Grafos
Aluna: Brenda Silva Machado
Algoritmo de Edmonds-Karp
"""

from grafo import Grafo

class edmondsKarp():
    def __init__(self, grafo : Grafo, s, t):
        self.grafo = grafo
        self.vertices = grafo.getVertices()
        self.capacidades = grafo.getFuncao()
        self.arcos = grafo.getArcos()
        self.s = s
        self.t = t
        self.rede_residual = self.criarRedeResidual()
        self.fluxo_maximo = self.calcularFluxoMaximo()

    def getFluxoMaximo(self):
        return self.fluxo_maximo
    
    def criarRedeResidual(self):
        temp_arcos = []
        temp_funcao = {}
        for arco in self.arcos:
            temp_arcos.append(arco)
            temp_funcao[arco] = self.capacidades[arco]
            temp_arcos.append((arco[1], arco[0]))
            temp_funcao[(arco[1], arco[0])] = 0
        rede_residual = Grafo(self.vertices, [], temp_funcao, temp_arcos)
        return rede_residual
    
    def calcularFluxoMaximo(self):
        fluxo_maximo = 0
        while True:
            caminho = self.buscarCaminho()
            print(caminho)
            if not caminho:
                break
            fluxo_maximo += int(self.aumentarFluxo(caminho))
        return fluxo_maximo
    
    def buscarCaminho(self):
        caminho = []
        fila = [self.s]
        visitados = [self.s]
        while fila:
            v = fila.pop(0)
            for u in self.rede_residual.vizinhos(v):
                if u not in visitados and int(self.rede_residual.peso(v, u)) > 0:
                    visitados.append(u)
                    fila.append(u)
                    caminho.append((v, u))
        return caminho if self.t in visitados else []
    
    def aumentarFluxo(self, caminho):
        fluxo = min(self.rede_residual.peso(v, u) for v, u in caminho) 
        for v, u in caminho:
            self.rede_residual.removerArco(v, u)
            self.rede_residual.adicionarArco(u, v)
            self.rede_residual.adicionarPeso(u, v, fluxo)
        return fluxo