
""" Arquivo de teste para demonstrar o funcionamento dos algoritmos
"""

from compFortementeConexas import compFortementeConexas
from ordenacaoTopologica import ordenacaoTopologica
from prim import Prim
from grafo import Grafo


grafo = Grafo(None, None, None, None)
grafo = grafo.ler('teste.txt')

# teste componentes fortemente conexas
comp = compFortementeConexas(grafo)
comp.run()
comp.print()

# # teste ordenacao topologica
ot = ordenacaoTopologica(grafo)
ot.ordenacao()
ot.print()

# teste prim 
grafo1 = Grafo(None, None, None, None)
grafo1 = grafo1.ler('agm_tiny.txt')
prim = Prim(grafo1)
prim.run()
prim.print()
