from algs4.point2d import Point2D
from algs4 import stddraw
import math

class RectHV:
    """
    The RectHV class is an immutable data type to encapsulate a
    two-dimensional axis-aligned rectagle with real-value coordinates.
    The rectangle is closed—it includes the points on the boundary.
    """

    def __init__(self, xmin, ymin, xmax, ymax):
        if math.isnan(xmin) or math.isnan(xmax) or math.isnan(ymin) or math.isnan(ymax):
            raise ValueError("Coordinates cannot be NaN")
        if xmax < xmin or ymax < ymin:
            raise ValueError("Invalid rectangle dimensions")
        
        self._xmin = xmin
        self._ymin = ymin
        self._xmax = xmax
        self._ymax = ymax

    def xmin(self):
        """Returns the minimum x-coordinate of any point in this rectangle."""
        return self._xmin

    def ymin(self):
        """Returns the minimum y-coordinate of any point in this rectangle."""
        return self._ymin

    def xmax(self):
        """Returns the maximum x-coordinate of any point in this rectangle."""
        return self._xmax

    def ymax(self):
        """Returns the maximum y-coordinate of any point in this rectangle."""
        return self._ymax

    def width(self):
        """Returns the width of this rectangle."""
        return self._xmax - self._xmin

    def height(self):
        """Returns the height of this rectangle."""
        return self._ymax - self._ymin

    def intersects(self, that):
        """Returns true if the two rectangles intersect."""
        return self._xmax >= that._xmin and self._ymax >= that._ymin and \
               that._xmax >= self._xmin and that._ymax >= self._ymin

    def contains(self, p: Point2D):
        """Returns true if this rectangle contains the point."""
        return (self._xmin <= p.x() <= self._xmax) and \
               (self._ymin <= p.y() <= self._ymax)

    def distance_to(self, p: Point2D):
        """Returns the Euclidean distance between this rectangle and the point p."""
        return math.sqrt(self.distance_squared_to(p))

    def distance_squared_to(self, p: Point2D):
        """Returns the square of the Euclidean distance between this rectangle and the point p."""
        dx = 0.0
        dy = 0.0
        if p.x() < self._xmin:
            dx = p.x() - self._xmin
        elif p.x() > self._xmax:
            dx = p.x() - self._xmax
        
        if p.y() < self._ymin:
            dy = p.y() - self._ymin
        elif p.y() > self._ymax:
            dy = p.y() - self._ymax
            
        return dx*dx + dy*dy

    def __eq__(self, other):
        if other == self: return True
        if other == None: return False
        if other.__class__ != self.__class__: return False
        return self._xmin == other._xmin and self._ymin == other._ymin and \
               self._xmax == other._xmax and self._ymax == other._ymax

    def __hash__(self):
        hash1 = hash(self._xmin)
        hash2 = hash(self._ymin)
        hash3 = hash(self._xmax)
        hash4 = hash(self._ymax)
        return 31 * (31 * (31 * hash1 + hash2) + hash3) + hash4
        
    def __str__(self):
        return f"[{self._xmin}, {self._xmax}] x [{self._ymin}, {self._ymax}]"

    def draw(self):
        """Draws this rectangle to standard draw."""
        stddraw.line(self._xmin, self._ymin, self._xmax, self._ymin)
        stddraw.line(self._xmax, self._ymin, self._xmax, self._ymax)
        stddraw.line(self._xmax, self._ymax, self._xmin, self._ymax)
        stddraw.line(self._xmin, self._ymax, self._xmin, self._ymin)
