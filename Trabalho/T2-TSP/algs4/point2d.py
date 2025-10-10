import math
import functools

# Importações circulares potenciais. Importar módulos inteiros para evitar.
from algs4 import stdrandom
from algs4 import stddraw

class Point2D:
    """
    The Point2D class is an immutable data type to encapsulate a
    two-dimensional point with real-value coordinates.
    """

    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numbers")
        if math.isinf(x) or math.isinf(y):
            raise ValueError("Coordinates must be finite")
        if math.isnan(x) or math.isnan(y):
            raise ValueError("Coordinates cannot be NaN")
        
        self.x_val = float(x)
        self.y_val = float(y)

    def x(self):
        """Returns the x-coordinate."""
        return self.x_val

    def y(self):
        """Returns the y-coordinate."""
        return self.y_val

    def r(self):
        """Returns the polar radius of this point."""
        return math.sqrt(self.x_val**2 + self.y_val**2)

    def theta(self):
        """Returns the angle of this point in polar coordinates."""
        return math.atan2(self.y_val, self.x_val)

    def _angle_to(self, that):
        """Returns the angle between this point and that point."""
        dx = that.x_val - self.x_val
        dy = that.y_val - self.y_val
        return math.atan2(dy, dx)

    @staticmethod
    def ccw(a, b, c):
        """
        Returns true if a→b→c is a counterclockwise turn.
        Returns { -1, 0, +1 } if a→b→c is a { clockwise, collinear; counterclockwise } turn.
        """
        area2 = (b.x_val - a.x_val) * (c.y_val - a.y_val) - \
                (b.y_val - a.y_val) * (c.x_val - a.x_val)
        if area2 < 0:
            return -1
        elif area2 > 0:
            return 1
        else:
            return 0

    @staticmethod
    def area2(a, b, c):
        """Returns twice the signed area of the triangle a-b-c."""
        return (b.x_val - a.x_val) * (c.y_val - a.y_val) - \
               (b.y_val - a.y_val) * (c.x_val - a.x_val)

    def distance_to(self, that):
        """Returns the Euclidean distance between this point and that point."""
        dx = self.x_val - that.x_val
        dy = self.y_val - that.y_val
        return math.sqrt(dx**2 + dy**2)

    def distance_squared_to(self, that):
        """Returns the square of the Euclidean distance between this point and that point."""
        dx = self.x_val - that.x_val
        dy = self.y_val - that.y_val
        return dx**2 + dy**2

    def __lt__(self, other):
        if self.y_val < other.y_val:
            return True
        if self.y_val > other.y_val:
            return False
        if self.x_val < other.x_val:
            return True
        return False
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if not isinstance(other, Point2D): return False
        return self.x_val == other.x_val and self.y_val == other.y_val

    def __str__(self):
        return f"({self.x_val}, {self.y_val})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return 31 * hash(self.x_val) + hash(self.y_val)

    def draw(self):
        """Plot this point using standard draw."""
        stddraw.point(self.x_val, self.y_val)

    def draw_to(self, that):
        """Plot a line from this point to that point using standard draw."""
        stddraw.line(self.x_val, self.y_val, that.x_val, that.y_val)

    def _polar_order_comparator(self, q1, q2):
        dx1 = q1.x_val - self.x_val
        dy1 = q1.y_val - self.y_val
        dx2 = q2.x_val - self.x_val
        dy2 = q2.y_val - self.y_val

        if dy1 >= 0 and dy2 < 0: return -1
        elif dy2 >= 0 and dy1 < 0: return 1
        elif dy1 == 0 and dy2 == 0:
            if dx1 >= 0 and dx2 < 0: return -1
            elif dx2 >= 0 and dx1 < 0: return 1
            else: return 0
        else:
            return -Point2D.ccw(self, q1, q2)

    def polar_order(self):
        return functools.cmp_to_key(self._polar_order_comparator)
        
def x_order(p, q):
    return p.x_val - q.x_val

def y_order(p, q):
    return p.y_val - q.y_val
    
def r_order(p, q):
    delta = (p.x_val**2 + p.y_val**2) - (q.x_val**2 + q.y_val**2)
    if delta < 0: return -1
    if delta > 0: return 1
    return 0
