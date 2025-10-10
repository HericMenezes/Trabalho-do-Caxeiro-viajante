# *****************************************************************************
# * VOCÊ NÃO PRECISA MODIFICAR ESTE ARQUIVO
# *
# * Executa a heurística de inserção pelo vizinho mais próximo para o problema
# * do caixeiro viajante e plota os resultados.
# ****************************************************************************

from algs4 import stdin, stdout, stddraw
from src_copy.tour import Tour
from src_copy.point import Point

def main():
    # obter dimensões
    width = stdin.read_int()
    height = stdin.read_int()
    border = 20
    stddraw.set_canvas_size(width, height + border)
    stddraw.set_xscale(0, width)
    stddraw.set_yscale(-border, height)

    # ativar modo de animação
    stddraw.enable_double_buffering()

    # executar a heurística de inserção pelo vizinho mais próximo
    tour = Tour()
    while not stdin.is_empty():
        x = stdin.read_double()
        y = stdin.read_double()
        p = Point(x, y)
        tour.insert_nearest(p)

        # descomente as 4 linhas abaixo para animar
        # stddraw.clear()
        # tour.draw()
        # stddraw.text(100, 0, f"comprimento = {tour.length():.2f}")
        # stddraw.show()
        # stddraw.pause(50)

    # desenhar no quadro padrão
    tour.draw()
    stddraw.show()
    
    # imprimir o ciclo no terminal padrão
    stdout.println(tour)
    stdout.printf("Comprimento do ciclo = %.4f\n", tour.length())
    stdout.printf("Número de pontos = %d\n", tour.size())

if __name__ == '__main__':
    main()
