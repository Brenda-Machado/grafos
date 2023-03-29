# Atividade Pratica A1 – Grafos (INE5413)
Ciencias da Computacao – Universidade Federal de Santa Catarina
Prof. Rafael de Santiago
## Observacoes gerais:
+ Trabalho deve ser executado em no maximo 3 estudantes da disciplina.
+ Todas as codificacoes devem estar em uma das seguintes linguagens de programacao: C/C++, Python ou Java.
+ A biblioteca de grafos criada no primeiro item desse exercıcio devera ser utilizada na codificacao dos demais itens dessa
atividade.
+ A entrega do codigo-fonte devera ser realizada no MOODLE
em um arquivo compactado no formato ZIP ou TAR.GZ.
+ A atividade vale 12 pts. Se o grupo preferir, pode deixar de fazer um dos itens, exceto o item 4 (Relatorio). As equipes que
atingirem mais de 10 pts no trabalho, receberao nota 10 e o saldo sera utilizado no proximo trabalho com nota inferior a 10
no semestre corrente.
+ Duas ou mais equipes com trabalhos total ou parcialmente iguais receberao nota 0.
+ A entrega deve ser realizada atraves do ambiente da turma no MOODLE.

## 1. [Representacao] (2,0pts) 
Crie um tipo estruturado de dados ou uma classe que represente um grafo nao-dirigido
e ponderado G(V, E, w), no qual V é o conjunto de vertices, E é o conjunto de arestas e w : E → R e a funcao que
mapeia o peso de cada aresta {u, v} ∈ E. As operacoes/metodos contemplados para o grafo deverao ser:
+ qtdVertices(): retornr a quantidade de vertices;
+ qtdArestas(): retorna a quantidade de arestas;
+ grau(v): retorna o grau do vertice v;
+ rotulo(v): retorna o rotulo do vertice v;
+ vizinhos(v): retorna os vizinhos do vertice v;
+ haAresta(u, v): se {u, v} ∈ E, retorna verdadeiro; se nao existir, retorna falso;
+ peso(u, v): se {u, v} ∈ E, retorna o peso da aresta {u, v}; se nao existir, retorna um valor infinito positivo;
+ ler(arquivo)2
Deve carregar um grafo a partir de um arquivo no formato especificado ao final deste documento.
IMPORTANTE: As operacoes/metodos deverao ter complexidade de tempo computacional O(1) quando possıvel.
No caso de duvidas, consulte o professor da disciplina.

## 2. [Buscas] (2,0pts) 
Crie um programa que receba um arquivo de grafo e o ındice do vertice s como argumentos. O
programa deve fazer uma busca em largura a partir de s e devera imprimir a saıda na tela, onde cada linha devera
conter o nıvel seguido de “:” e a listagem de vertices encontrados naquele nıvel. O exemplo abaixo trata de uma
saıda, na qual a busca se iniciou pelo vertice s no nıvel 0, depois prosseguiu nos vertices 3, 4 e 5 para o proximo
nıvel. No nıvel seguinte, a busca encontrou os vertices 1, 2, 6 e 7.


> 0: 8
> 1: 3,4,5
> 2: 1,2,6,7

## 3. [Ciclo Euleriano] (2,0pts) 
Crie um programa que recebe um grafo como argumento. Ao final, o programa devera
determinar se ha ou nao um ciclo euleriano e exibı-lo na tela de acordo com o exemplo abaixo. A primeira linha
devera conter o numero 0 caso o grafo nao contenha o ciclo euleriano. Caso contenha, devera ser impresso 1 na
O valor infinito pode ser representado como o maior ponto flutuante positivo possıvel de ser caracterizado pelo tipo de dado selecionado.
+ Para linguagens orientadas a objetos, a operacao ler(arquivo) pode ser substituıda por um construtor.
+ Entende-se como ındice do vertice um dos valores de 1 a n definidos no arquivo do grafo de entrada.
+ Ignore os pesos do arquivo de entrada, pois a busca nao precisara deles.
+ Ignore os pesos do arquivo de entrada, pois nao serao necessarios.
+ primeira linha e em seguida, a sequencia de vertices que corresponde ao ciclo devera ser impressa.

> 2,4,3,1,5,6,2

## 4. [Algoritmo de Bellman-Ford ou de Dijkstra] (2,0pts) 
Crie um programa que recebe um arquivo de grafo como
argumento e um vertice s. O programa devera executar o algoritmo de Bellman-Ford ou de Dijkstra e informar o
caminho percorrido de s ate todos os outros vertices do grafo e a distancia necessaria. A saıda devera ser impressa
na tela de acordo com o exemplo abaixo. Cada linha representa o caminho realizado de s para o vertice da respectiva
linha. Em cada linha, antes dos sımbolo “:” devera estar o vertice destino. A direita de “:”, encontra-se o caminho 
percorrido de s ate o vertice destino. Mais a direita encontram-se os sımbolos “d=” seguidos da distancia necessaria
para percorrer o caminho.
> 1: 2,3,4,1; d=7
> 2: 2; d=0
> 3: 2,3; d=4
> 4: 2,3,4; d=6
> 5: 2,3,5; d=8

## 5. [Algoritmo de Floyd-Warshall] (2,0pts) 
Crie um programa que recebe um arquivo de grafo como argumento. O
programa devera exercutar o algoritmo de Floyd-Warshall e mostrar as distancias para cada par de vertices na tela
utilizando o formato do exemplo abaixo. Na saıda, cada linha tera as distancias para vertice na ordem crescente
dos ındices informados no arquivo de entrada.
> 1:0,10,3,5
> 2:10,0,9,8
> 3:3,9,0,11
> 4:5,8,11,0

## 6. [Relatorio] (2,0pts) 
Elabore um relatorio de uma pagina no formato PDF comentando para cada um dos exercıcios
quais as estruturas de dados selecionadas, justificando as escolhas. Nao esqueca de informar os nomes dos integrantes
da equipe.
### Padrao de Arquivo de Entrada
O arquivo de entrada deve estar no formato abaixo. 
Na primeira linha, n e o numero de vertices. Nas linhas seguintes e antes da palavra “*edges”, ha uma listagem de rotulos dos vertices. Note que cada vertice possui um ındice de 1 a n. Esse ındice e importante, pois ele e utilizado nas definicoes das arestas. Depois da palavra “*edges” cada linha contera
uma aresta. Por exemplo, na linha onde ha “a b valor do peso”, a e b sao os vertices que a aresta conecta, valor do peso
e o peso da aresta.

> *vertices n
> 1 rotulo_de_1
> 2 rotulo_de_2
> ...
> n label_de_n
> *edges
> a b valor_do_peso
> a c valor_do_peso
> ...
> 2