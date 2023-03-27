# Atividade Pratica A1 – Grafos (INE5413)
Ciencias da Computacao – Universidade Federal de Santa Catarina
Prof. Rafael de Santiago
## Observacoes gerais:
+ Trabalho deve ser executado em no m´aximo 3 estudantes da disciplina.
+ Todas as codificacoes devem estar em uma das seguintes linguagens de programacao: C/C++, Python ou Java.
+ A biblioteca de grafos criada no primeiro item desse exerc´ıcio dever´a ser utilizada na codifica¸c˜ao dos demais itens dessa
atividade.
+ A entrega do codigo-fonte devera ser realizada no MOODLE
em um arquivo compactado no formato ZIP ou TAR.GZ.
+ A atividade vale 12 pts. Se o grupo preferir, pode deixar de fazer um dos itens, exceto o item 4 (Relat´orio). As equipes que
atingirem mais de 10 pts no trabalho, receberao nota 10 e o saldo ser´a utilizado no pr´oximo trabalho com nota inferior a 10
no semestre corrente.
+ Duas ou mais equipes com trabalhos total ou parcialmente iguais receberao nota 0.
+ A entrega deve ser realizada atraves do ambiente da turma no MOODLE.

## 1. [Representacao] (2,0pts) 
Crie um tipo estruturado de dados ou uma classe que represente um grafo n˜ao-dirigido
e ponderado G(V, E, w), no qual V ´e o conjunto de v´ertices, E ´e o conjunto de arestas e w : E → R ´e a fun¸c˜ao que
mapeia o peso de cada aresta {u, v} ∈ E. As opera¸c˜oes/m´etodos contemplados para o grafo dever˜ao ser:
+ qtdVertices(): retornr a quantidade de v´ertices;
+ qtdArestas(): retorna a quantidade de arestas;
+ grau(v): retorna o grau do v´ertice v;
+ rotulo(v): retorna o r´otulo do v´ertice v;
+ vizinhos(v): retorna os vizinhos do v´ertice v;
+ haAresta(u, v): se {u, v} ∈ E, retorna verdadeiro; se n˜ao existir, retorna falso;
+ peso(u, v): se {u, v} ∈ E, retorna o peso da aresta {u, v}; se n˜ao existir, retorna um valor infinito positivo;
+ ler(arquivo)2
Deve carregar um grafo a partir de um arquivo no formato especificado ao final deste documento.
IMPORTANTE: As operacoes/metodos deverao ter complexidade de tempo computacional O(1) quando possıvel.
No caso de duvidas, consulte o professor da disciplina.

## 2. [Buscas] (2,0pts) 
Crie um programa que receba um arquivo de grafo e o ´ındice do v´ertice s como argumentos. O
programa deve fazer uma busca em largura4 a partir de s e dever´a imprimir a sa´ıda na tela, onde cada linha dever´a
conter o n´ıvel seguido de “:” e a listagem de v´ertices encontrados naquele n´ıvel. O exemplo abaixo trata de uma
sa´ıda, na qual a busca se iniciou pelo v´ertice s no n´ıvel 0, depois prosseguiu nos v´ertices 3, 4 e 5 para o pr´oximo
n´ıvel. No n´ıvel seguinte, a busca encontrou os v´ertices 1, 2, 6 e 7.


> 0: 8
> 1: 3,4,5
> 2: 1,2,6,7

## 3. [Ciclo Euleriano] (2,0pts) 
Crie um programa que recebe um grafo como argumento. Ao final, o programa dever´a
determinar se h´a ou n˜ao um ciclo euleriano e exib´ı-lo na tela de acordo com o exemplo abaixo. A primeira linha
dever´a conter o n´umero 0 caso o grafo n˜ao contenha o ciclo euleriano. Caso contenha, dever´a ser impresso 1 na
O valor infinito pode ser representado como o maior ponto flutuante positivo poss´ıvel de ser caracterizado pelo tipo de dado selecionado.
+ Para linguagens orientadas a objetos, a opera¸c˜ao ler(arquivo) pode ser substitu´ıda por um construtor.
+ Entende-se como ´ındice do v´ertice um dos valores de 1 a n definidos no arquivo do grafo de entrada.
+ Ignore os pesos do arquivo de entrada, pois a busca n˜ao precisar´a deles.
+ Ignore os pesos do arquivo de entrada, pois n˜ao ser˜ao necess´arios.
+ primeira linha e em seguida, a sequˆencia de v´ertices que corresponde ao ciclo dever´a ser impressa.

> 2,4,3,1,5,6,2

## 4. [Algoritmo de Bellman-Ford ou de Dijkstra] (2,0pts) 
Crie um programa que recebe um arquivo de grafo como
argumento e um v´ertice s. O programa dever´a executar o algoritmo de Bellman-Ford ou de Dijkstra e informar o
caminho percorrido de s at´e todos os outros v´ertices do grafo e a distˆancia necess´aria. A sa´ıda dever´a ser impressa
na tela de acordo com o exemplo abaixo. Cada linha representa o caminho realizado de s para o v´ertice da respectiva
linha. Em cada linha, antes dos s´ımbolo “:” dever´a estar o v´ertice destino. A direita de “:”, encontra-se o caminho `
percorrido de s at´e o v´ertice destino. Mais `a direita encontram-se os s´ımbolos “d=” seguidos da distˆancia necess´aria
para percorrer o caminho.
> 1: 2,3,4,1; d=7
> 2: 2; d=0
> 3: 2,3; d=4
> 4: 2,3,4; d=6
> 5: 2,3,5; d=8

## 5. [Algoritmo de Floyd-Warshall] (2,0pts) 
Crie um programa que recebe um arquivo de grafo como argumento. O
programa dever´a exercutar o algoritmo de Floyd-Warshall e mostrar as distˆancias para cada par de v´ertices na tela
utilizando o formato do exemplo abaixo. Na sa´ıda, cada linha ter´a as distˆancias para v´ertice na ordem crescente
dos ´ındices informados no arquivo de entrada.
> 1:0,10,3,5
> 2:10,0,9,8
> 3:3,9,0,11
> 4:5,8,11,0

## 6. [Relat´orio] (2,0pts) 
Elabore um relat´orio de uma p´agina no formato PDF comentando para cada um dos exerc´ıcios
quais as estruturas de dados selecionadas, justificando as escolhas. N˜ao esque¸ca de informar os nomes dos integrantes
da equipe.
### Padr˜ao de Arquivo de Entrada
O arquivo de entrada deve estar no formato abaixo. 
Na primeira linha, n ´e o n´umero de v´ertices. Nas linhas seguintes e antes da palavra “*edges”, h´a uma listagem de r´otulos dos v´ertices. Note que cada v´ertice possui um ´ındice de 1 `a n. Esse ´ındice ´e importante, pois ele ´e utilizado nas defini¸c˜oes das arestas. Depois da palavra “*edges” cada linha conter´a
uma aresta. Por exemplo, na linha onde h´a “a b valor do peso”, a e b s˜ao os v´ertices que a aresta conecta, valor do peso
´e o peso da aresta.

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