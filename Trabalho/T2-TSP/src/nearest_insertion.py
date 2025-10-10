# *****************************************************************************
# * Cliente que executa a heurística do vizinho mais próximo.
# ****************************************************************************

from algs4 import stdin, stdout, stddraw
from src.tour import Tour
from src.point import Point

def main():
    try:
        width = stdin.read_int()
        height = stdin.read_int()
        border = 20
        stddraw.set_canvas_size(width, height + border)
        stddraw.set_xscale(0, width)
        stddraw.set_yscale(-border, height)
        stddraw.enable_double_buffering()

        tour = Tour()
        while not stdin.is_empty():
            x = stdin.read_double()
            y = stdin.read_double()
            p = Point(x, y)
            tour.insert_nearest(p)

        tour.draw()
        stddraw.show()
        stdout.println(tour)
        stdout.printf("Comprimento do ciclo = %.4f\n", tour.length())
        stdout.printf("Número de pontos = %d\n", tour.size())
    except NotImplementedError as e:
        print(f"Execução interrompida pois uma função em Tour não foi implementada: {e}")
    except EOFError:
        print("Entrada padrão vazia. Execute com dados de entrada, ex: python -m src.nearest_insertion < data/tsp10.txt")

if __name__ == '__main__':
    main()
