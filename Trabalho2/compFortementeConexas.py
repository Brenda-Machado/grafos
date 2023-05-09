"""
Trabalho 2 - Grafos
Aluna: Brenda Silva Machado
Exercício 1 - Representação de Componentes Fortemente Conexas
"""

from Trabalho1.grafo import Grafo
from DFS import DFS


# 1. [Componentes Fortemente Conexas] (3,0pts) 
#Crie um programa que receba um grafo dirigido e nao-ponderado como argumento. Ao final, imprima na tela as componentes fortemente conexas desse grafo. 
# O exemplo abaixo trata de uma saıda valida, na qual identificou-se duas componentes fortemente conexas {3, 4, 5} e {1, 2, 6, 7}.

##> 3,4,5
##> 1,2,6,7

class compFortementeConexas:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.T = DFS(grafo)
        self.G_trans = self.grafo.transposto() # TO-DO
        self.T_inv = DFS.dfs_adaptado(self.G_trans) # TO-DO
        self.componentes = {}
    

    