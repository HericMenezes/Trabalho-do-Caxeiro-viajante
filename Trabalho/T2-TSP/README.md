# Projeto Base – TSP (Vizinho Mais Próximo) em Python

Template para implementar a heurística do vizinho mais próximo no Problema do Caixeiro Viajante (TSP) utilizando Python. As atividades estão divididas em duas etapas: começar com a versão ingênua e, em seguida, otimizar com `KdTree`.

## Objetivo
1. Implementar o método `_insert_nearest_naive` em `tour.py`, varrendo a lista encadeada circular para encontrar o vizinho mais próximo.
2. Implementar a classe `KdTree` em `algs4/kd_tree.py` e adaptar o método `insert_nearest` para utilizar a busca otimizada, reduzindo o custo de busca.
3. Preencher `questoes.txt` com respostas conceituais, comprimentos de tour e medições de tempo (comparando as duas abordagens).

## Estrutura do Template
- `src/`: Contém as classes principais do projeto (`tour`, `point`, `nearest_insertion`, `tsp_visualizer`, `tsp_timer`).
- `algs4/`: Contém os módulos utilitários da biblioteca algs4 traduzidos para Python, incluindo um stub de `kd_tree.py`.
- `data/`: Coloque aqui os arquivos de teste (p. ex. `tsp10.txt`, `tsp100.txt`, ...).
- `results/`: Contém referências de saída para `tsp10.txt`.

## Fluxo Sugerido
1. Complete os métodos faltantes na classe `Tour` utilizando a busca ingênua e valide sua implementação com o script `nearest_insertion`.
2. Implemente a classe `KdTree` e a versão otimizada do método de inserção. Compare os tempos de execução usando `tsp_timer` (a semente está fixa em `stdrandom.set_seed(123456789)`).
3. Atualize o arquivo `questoes.txt` com os comprimentos de ciclo obtidos e as tabelas de tempo comparando a abordagem ingênua vs. `KdTree`.

## Instalação de Dependências
Este projeto utiliza as bibliotecas `matplotlib` e `numpy` para a visualização gráfica. Para instalá-las, execute:
```bash
pip install matplotlib numpy
```

## Execução
- Heurística: `python -m src.nearest_insertion < data/tsp10.txt`
- Visualizador: `python -m src.tsp_visualizer data/tsp1000.txt`
- Temporizador: `python -m src.tsp_timer 1000`

## Referências de resultado
- `results/tsp10-nearest.ans`: evolução do tour gerado pela heurística nearest (útil para depurar).
- `results/tsp10-optimal.ans`: solução ótima conhecida para comparação.

## Entrega
Submeta `tour.py` e `questoes.txt` preenchidos com as análises solicitadas.

