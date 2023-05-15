from compFortementeConexas import compFortementeConexas
from grafo import Grafo

grafo = Grafo(None, None, None, None)
grafo = grafo.ler('teste.txt')
comp = compFortementeConexas(grafo)
comp.run()
comp.print()
