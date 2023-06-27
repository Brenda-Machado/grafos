from grafo import Grafo
from edmondsKarp import edmondsKarp
from hopcroftKarp import hopcroftKarp
from grafoBipartido import grafoBipartido
from lawler import Lawler

# TESTE FLUXO MÁXIMO F = 2
# grafo = Grafo(None, None, None, None)
# grafo = grafo.ler('fluxo_maximo_aula.txt')
# edK = edmondsKarp(grafo, grafo.getS(), grafo.getT())
# print(edK.getFluxoMaximo())

# TESTE EMPARELHAMENTO M = 0
grafo_bip = grafoBipartido(None, None)
grafo_bip = grafo_bip.ler('pequeno.txt')
hpK = hopcroftKarp(grafo_bip)
max_matching = hpK.getMatching()
mate = hpK.getMate()
print(max_matching, mate)

# TESTE COLORAÇÃO M = 3
# grafo = Grafo(None, None, None, None)
# grafo = grafo.ler('cor3.txt')
# lawler = Lawler(grafo)
# print(lawler.calculaColoracaoMinima())


