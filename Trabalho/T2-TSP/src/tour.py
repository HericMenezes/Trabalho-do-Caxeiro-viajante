from algs4 import stddraw, stdout
from src.point import Point

# A KdTree não foi implementada ainda, então criamos uma classe provisória.
# Substitua pela sua implementação de algs4.kd_tree quando estiver pronta.
try:
    from algs4.kd_tree import KdTree
except ImportError:
    class KdTree:
        def __init__(self): pass

class Tour:
    """
    Template da classe Tour para a heurística do vizinho mais próximo.

    Primeira etapa sugerida:
     - implemente os métodos de lista encadeada e chame insertNearestNaive(Point).
    Segunda etapa:
     - implemente a classe algs4.KdTree e utilize insertNearestKd(Point)
       para acelerar a busca do vizinho mais próximo.
    """
    
    class _Node:
        def __init__(self, point=None, next_node=None):
            self.point = point
            self.next = next_node

    def __init__(self, use_kd_tree=False):
        self._use_kd_tree = use_kd_tree
        self._start = None
        self._count = 0
        if self._use_kd_tree:
            self._kd_tree = KdTree()

    def size(self):
        raise NotImplementedError("Implementar size()")

    def length(self):
        raise NotImplementedError("Implementar length()")

    def __str__(self):
        raise NotImplementedError("Implementar toString()")

    def draw(self):
        raise NotImplementedError("Implementar draw()")

    def insert_nearest(self, p: Point):
        if self._use_kd_tree:
            self._insert_nearest_kd(p)
        else:
            self._insert_nearest_naive(p)
    
    def _insert_nearest_naive(self, p: Point):
        """
        Versão ingênua: percorre toda a lista, calcula a distância para cada nó
        usando Point.distanceTo(Point) e insere o novo ponto após o vizinho
        mais próximo encontrado.
        """
        raise NotImplementedError("Implementar insertNearestNaive(Point)")
    
    def _insert_nearest_kd(self, p: Point):
        """
        Versão otimizada: utiliza o KdTree para localizar rapidamente o
        ponto mais próximo e insere o novo nó na lista. Requer que a classe
        algs4.KdTree esteja totalmente implementada.
        """
        raise NotImplementedError("Implementar insertNearestKd(Point)")

def main():
    tour = Tour()
    try:
        tour.insert_nearest(Point(1.0, 1.0))
        tour.insert_nearest(Point(1.0, 4.0))
        tour.insert_nearest(Point(4.0, 4.0))
        tour.insert_nearest(Point(4.0, 1.0))

        stdout.println(f"# de pontos = {tour.size()}")
        stdout.println(f"Comprimento = {tour.length()}")
        stdout.println(tour)

        stddraw.set_xscale(0, 6)
        stddraw.set_yscale(0, 6)
        tour.draw()
        stddraw.show()
    except NotImplementedError as e:
        print(f"Execução de main() em tour.py interrompida pois uma função não foi implementada: {e}")


if __name__ == '__main__':
    main()
