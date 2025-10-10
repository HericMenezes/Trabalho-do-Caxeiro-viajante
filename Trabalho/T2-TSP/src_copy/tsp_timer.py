# *****************************************************************************
# * VOCÊ NÃO PRECISA MODIFICAR ESTE ARQUIVO
# *
# * Mede o tempo da heurística do vizinho mais próximo gerando instâncias 
# * aleatórias de tamanho n.
# ****************************************************************************

import sys
from algs4 import stdrandom, stopwatch, stdout
from src_copy.point import Point
from src_copy.tour import Tour

def main():
    lo = 0.0
    hi = 600.0
    
    if len(sys.argv) < 2:
        print("Uso: python -m src_copy.tsp_timer <numero_de_pontos>")
        return
        
    n = int(sys.argv[1])

    # gerar dados e executar a heurística de inserção pelo vizinho mais próximo
    stdrandom.set_seed(123456789)
    timer1 = stopwatch.Stopwatch()
    tour1 = Tour()
    for _ in range(n):
        x = stdrandom.uniform_double(lo, hi)
        y = stdrandom.uniform_double(lo, hi)
        p = Point(x, y)
        tour1.insert_nearest(p)
    
    length1 = tour1.length()
    elapsed1 = timer1.elapsed_time()
    
    stdout.println(f"Comprimento do ciclo = {length1}")
    stdout.println(f"Inserção pelo vizinho mais próximo: {elapsed1} segundos")
    stdout.println()
    stdout.println("Inserção pelo menor aumento: funcionalidade removida")

if __name__ == '__main__':
    main()
