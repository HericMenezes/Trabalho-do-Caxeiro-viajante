from algs4 import stddraw, stdout
from algs4.point2d import Point2D
from algs4.kd_tree import KdTree
from src_copy.point import Point

class Tour:
    """
    Descrição: Esta classe define o tipo de dado Tour implementando uma
    Lista Encadeada Circular e definindo métodos para permitir a implementação
    da heurística para encontrar boas soluções para o TSP.
    """
    
    class _Node:
        def __init__(self, point=None, next_node=None):
            self.point = point
            self.next = next_node

    def __init__(self, a=None, b=None, c=None, d=None):
        self._start = None
        self._count = 0
        self._kd_tree = KdTree()
        self._point_to_node = {}
        
        if all(isinstance(p, Point) for p in [a, b, c, d]):
            # Construtor de depuração com 4 pontos
            node_a = self._Node(a)
            node_b = self._Node(b)
            node_c = self._Node(c)
            node_d = self._Node(d)

            node_a.next = node_b
            node_b.next = node_c
            node_c.next = node_d
            node_d.next = node_a

            self._start = node_a
            self._count = 4
            
            self._register_node(node_a)
            self._register_node(node_b)
            self._register_node(node_c)
            self._register_node(node_d)

    def size(self):
        # retorna o número de pontos neste ciclo
        return self._count

    def length(self):
        # retorna o comprimento deste ciclo
        if self._start is None:
            return 0.0
        
        total = 0.0
        current = self._start
        for _ in range(self._count):
            total += current.point.distance_to(current.next.point)
            current = current.next
        return total

    def __str__(self):
        # retorna uma representação em string deste ciclo
        if self._start is None:
            return ""
        
        builder = []
        current = self._start
        for _ in range(self._count):
            builder.append(str(current.point))
            current = current.next
        return "\n".join(builder)

    def draw(self):
        # desenha este ciclo na tela padrão
        if self._start is None or self._start.next is None:
            return
            
        current = self._start
        for _ in range(self._count):
            current.point.draw_to(current.next.point)
            current = current.next

    def insert_nearest(self, p: Point):
        # insere p usando a heurística do vizinho mais próximo
        if p is None:
            raise ValueError("Ponto inválido")
        
        if self._start is None:
            node = self._Node(p)
            node.next = node
            self._start = node
            self._count = 1
            self._register_node(node)
            return

        query = Point2D(p.x, p.y)
        if self._kd_tree.is_empty():
            best_node = self._start
        else:
            nearest_point2d = self._kd_tree.nearest(query)
            best_node = None
            current = self._start
            for _ in range(self._count):
                if current.point.x == nearest_point2d.x() and current.point.y == nearest_point2d.y():
                    best_node = current
                    break
                current = current.next
        
        if best_node is None:
            best_node = self._start # Fallback

        new_node = self._Node(p)
        new_node.next = best_node.next
        best_node.next = new_node
        self._count += 1
        self._register_node(new_node)
        
    def _register_node(self, node: _Node):
        point2d = Point2D(node.point.x, node.point.y)
        self._point_to_node[node.point] = node
        if not self._kd_tree.contains(point2d):
            self._kd_tree.insert(point2d)

def main():
    # define 4 pontos, vértices de um quadrado
    a = Point(1.0, 1.0)
    b = Point(1.0, 4.0)
    c = Point(4.0, 4.0)
    d = Point(4.0, 1.0)

    # cria o ciclo a -> b -> c -> d -> a
    square_tour = Tour(a, b, c, d)

    # imprime o número de pontos na saída padrão
    size = square_tour.size()
    stdout.println(f"# de pontos = {size}")

    # imprime o comprimento do ciclo na saída padrão
    length = square_tour.length()
    stdout.println(f"Comprimento do ciclo = {length}")

    # imprime o ciclo na saída padrão
    stdout.println(square_tour)

    stddraw.set_xscale(0, 6)
    stddraw.set_yscale(0, 6)
    
    stddraw.enable_double_buffering()
    square_tour.draw()
    
    e = Point(5.0, 6.0)
    square_tour.insert_nearest(e)
    stddraw.clear()
    square_tour.draw()
    stddraw.show()

main()

if __name__ == "__main__":
    pass
