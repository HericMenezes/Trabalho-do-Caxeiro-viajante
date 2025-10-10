from algs4.point2d import Point2D

class KdTree:
    """
    Estrutura KdTree a ser implementada pelo aluno.
    """
    def __init__(self):
        raise NotImplementedError("implementar construtor")

    def is_empty(self):
        raise NotImplementedError("implementar isEmpty()")

    def size(self):
        raise NotImplementedError("implementar size()")

    def insert(self, p: Point2D):
        raise NotImplementedError("implementar insert(Point2D)")

    def contains(self, p: Point2D):
        raise NotImplementedError("implementar contains(Point2D)")

    def nearest(self, p: Point2D):
        raise NotImplementedError("implementar nearest(Point2D)")
