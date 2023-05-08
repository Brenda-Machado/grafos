
# Atividade A2 – Grafos (INE5413)

Ciencias da Computacao – Universidade Federal de Santa Catarina

## Observacoes gerais:

    + Trabalho deve ser executado em no maximo 3 estudantes da disciplina.

    + Todas as codificacoes devem estar em uma das seguintes linguagens de programacao: C/C++, Python ou Java.

    + A biblioteca de grafos criada na Atividade 1 devera ser utilizada na codificacao dos demais itens dessa atividade.

    + A entrega do codigo-fonte devera ser realizada no MOODLE em um arquivo compactado no formato ZIP ou TAR.GZ.

    + A entrega do relatorio  ́e obrigatorio e deve estar no formato PDF.

    + A atividade vale 12 pts. As equipes que atingirem mais de 10 pts no trabalho, receberao nota 10 e o saldo sera utilizado no proximo trabalho com nota inferior a 10 no semestre corrente.

    + Duas ou mais equipes com trabalhos total ou parcialmente iguais receberao nota 0.

    + A entrega deve ser realizada atraves do ambiente da turma no MOODLE.

## 1. [Componentes Fortemente Conexas] (3,0pts) 
Crie um programa que receba um grafo dirigido e nao-ponderado como argumento. Ao final, imprima na tela as componentes fortemente conexas desse grafo. O exemplo abaixo trata de uma saıda valida, na qual identificou-se duas componentes fortemente conexas {3, 4, 5} e {1, 2, 6, 7}.

> 3,4,5
> 1,2,6,7

## 2. [Ordenacao Topologica] (3,0pts) 
Crie um programa que receba um arquivo de grafo dirigido nao-ponderado com vertices rotulados como argumento. O programa deve fazer executar uma Ordena ̧c ̃ao Topologica. Depois exiba a ordem topologica, utilizando os rotulos de cada vertice, como no exemplo abaixo:

> Acordar → DesligarDespertador → CalcarSandalias → LevantarDaCama → TomarBanho → EscovarOsDentes → PrepararCafe → PrepararOvosMexidos → TomarCafeDaManha → LavarLoucas → EscovarOsDentes → CalcarMeias → VestirUniforme → ColocarSapato → FecharCasa.

## 3. [Kruskal ou Prim] (3,0pts) 
Crie um programa que recebe um grafo nao-dirigido e ponderado como argumento. Ao final, o programa devera determinar qual a arvore geradora ḿınima. O programa devera imprimir o somatorio das arestas na arvore na primeira linha e as arestas que pertencem a ́arvore geradora mınima na segunda linha,
como no exemplo abaixo:

> 22
> 5-4, 0-1, 2-3, 3-0, 4-1

## 4. [Relatorio] (3,0pts) 
Elabore um relatorio de uma pagina comentando para cada um dos exercıcios quais as estruturas de dados selecionadas, justificando as escolhas. Nao esqueca de informar os nomes dos integrantes da equipe.

## Padr ̃ao de Arquivo de Entrada
O arquivo de entrada deve estar no formato abaixo. Na primeira linha, n  ́e o numero de vertices. Nas linhas seguintes
e antes da palavra “*edges”, ha uma listagem de rotulos dos vertices. Note que cada v ́ertice possui um  ́ındice de 1 `a n.
Esse  ́ındice  ́e importante, pois ele  ́e utilizado nas definicoes das arestas. Depois da palavra “*edges” cada linha contera
uma aresta. Por exemplo, na linha onde ha “a b valor do peso”, a e b s ̃ao os vertices que a aresta conecta, valor do peso
e o peso da aresta.

> 1
> Para o caso de grafos dirigidos, a palavra “*arcs” aparece no lugar de “*edges”.
> *vertices n
> 1 rotulo_de_1
> 2 rotulo_de_2
> ...
> n label_de_n
> *edges
> a b valor_do_peso
> a c valor_do_peso
> ...
