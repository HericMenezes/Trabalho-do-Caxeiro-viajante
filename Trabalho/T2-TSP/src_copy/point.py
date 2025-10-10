# *****************************************************************************
# * NÃO MODIFIQUE OU SUBMETA ESTE ARQUIVO.
# *
# * Retirado da Seção 3.2, An Introduction to Programming (in Java)
# * por Robert Sedgewick e Kevin Wayne
# *
# * Tipo de dado imutável para pontos 2D com coordenadas de ponto flutuante.
# ****************************************************************************

import math
from algs4 import stddraw, stdin

class Point:
    def __init__(self, x: float, y: float):
        # cria e inicializa um ponto com (x, y) dados
        self._x = x
        self._y = y

    def distance_to(self, that: 'Point') -> float:
        # retorna a distância euclidiana entre dois pontos
        dx = self._x - that._x
        dy = self._y - that._y
        return math.sqrt(dx*dx + dy*dy)

    def draw(self) -> None:
        # desenha este ponto na tela padrão
        stddraw.point(self._x, self._y)

    def draw_to(self, that: 'Point') -> None:
        # desenha o segmento de linha entre este ponto e outro na tela padrão
        stddraw.line(self._x, self._y, that._x, that._y)

    def __str__(self) -> str:
        # retorna uma representação em string deste ponto
        return f"({self._x}, {self._y})"

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

def main():
    # lê um arquivo TSP da entrada padrão
    # e plota os pontos na tela padrão

    # obtém as dimensões
    width = stdin.read_int()
    height = stdin.read_int()
    stddraw.set_canvas_size(width, height)
    stddraw.set_xscale(0, width)
    stddraw.set_yscale(0, height)
    stddraw.set_pen_radius(0.005)

    # lê e plota os pontos um por vez
    while not stdin.is_empty():
        x = stdin.read_double()
        y = stdin.read_double()
        p = Point(x, y)
        p.draw()
    
    stddraw.show()

if __name__ == "__main__":
    main()
