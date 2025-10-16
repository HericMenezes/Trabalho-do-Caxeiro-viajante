package algs4;

public class KdTree {
    private static final double MIN = -1e12;
    private static final double MAX = 1e12;

    private Node root;
    private int size;

    private static class Node {
        private final Point2D p;
        private final RectHV rect;
        private Node lb; // left/bottom
        private Node rt; // right/top

        Node(Point2D p, RectHV rect) {
            this.p = p;
            this.rect = rect;
        }
    }

    public KdTree() {
        this.root = null;
        this.size = 0;
    }

    public boolean isEmpty() {
        return root == null;
    }

    public int size() {
        return size;
    }

    public void insert(Point2D p) {
        if (p == null)
            throw new IllegalArgumentException("point is null");
        if (root == null) {
            root = new Node(p, new RectHV(MIN, MIN, MAX, MAX));
            size = 1;
            return;
        }
        insert(root, p, true);
    }

    private void insert(Node n, Point2D p, boolean vertical) {
        if (n.p.equals(p))
            return; // ignore duplicate

        if (vertical) {
            if (p.x() < n.p.x()) {
                if (n.lb == null) {
                    RectHV r = new RectHV(n.rect.xmin(), n.rect.ymin(), n.p.x(), n.rect.ymax());
                    n.lb = new Node(p, r);
                    size++;
                } else
                    insert(n.lb, p, !vertical);
            } else {
                if (n.rt == null) {
                    RectHV r = new RectHV(n.p.x(), n.rect.ymin(), n.rect.xmax(), n.rect.ymax());
                    n.rt = new Node(p, r);
                    size++;
                } else
                    insert(n.rt, p, !vertical);
            }
        } else { // horizontal split
            if (p.y() < n.p.y()) {
                if (n.lb == null) {
                    RectHV r = new RectHV(n.rect.xmin(), n.rect.ymin(), n.rect.xmax(), n.p.y());
                    n.lb = new Node(p, r);
                    size++;
                } else
                    insert(n.lb, p, !vertical);
            } else {
                if (n.rt == null) {
                    RectHV r = new RectHV(n.rect.xmin(), n.p.y(), n.rect.xmax(), n.rect.ymax());
                    n.rt = new Node(p, r);
                    size++;
                } else
                    insert(n.rt, p, !vertical);
            }
        }
    }

    public boolean contains(Point2D p) {
        if (p == null)
            throw new IllegalArgumentException("point is null");
        return contains(root, p, true);
    }

    private boolean contains(Node n, Point2D p, boolean vertical) {
        if (n == null)
            return false;
        if (n.p.equals(p))
            return true;
        if (vertical) {
            if (p.x() < n.p.x())
                return contains(n.lb, p, !vertical);
            else
                return contains(n.rt, p, !vertical);
        } else {
            if (p.y() < n.p.y())
                return contains(n.lb, p, !vertical);
            else
                return contains(n.rt, p, !vertical);
        }
    }

    public Point2D nearest(Point2D p) {
        if (p == null)
            throw new IllegalArgumentException("point is null");
        if (root == null)
            return null;
        return nearest(root, p, root.p, root.p.distanceSquaredTo(p));
    }

    private Point2D nearest(Node n, Point2D q, Point2D best, double best2) {
        if (n == null)
            return best;
        // prune by rectangle
        double rectDist2 = n.rect.distanceSquaredTo(q);
        if (rectDist2 >= best2)
            return best;

        // check current point
        double d2 = n.p.distanceSquaredTo(q);
        if (d2 < best2) {
            best = n.p;
            best2 = d2;
        }

        // decide which subtree to visit first by rect distance
        Node first = n.lb, second = n.rt;
        double dFirst = first != null ? first.rect.distanceSquaredTo(q) : Double.POSITIVE_INFINITY;
        double dSecond = second != null ? second.rect.distanceSquaredTo(q) : Double.POSITIVE_INFINITY;
        if (dSecond < dFirst) { // swap to visit closer rect first
            first = n.rt;
            second = n.lb;
            double tmp = dFirst;
            dFirst = dSecond;
            dSecond = tmp;
        }

        if (first != null)
            best = nearest(first, q, best, best2 = best.distanceSquaredTo(q));
        if (second != null && second.rect.distanceSquaredTo(q) < best.distanceSquaredTo(q)) {
            best = nearest(second, q, best, best.distanceSquaredTo(q));
        }
        return best;
    }

    private int compare(Point2D p, Node n, boolean vertical) {
        if (vertical) {
            double cmp = p.x() - n.p.x();
            return (cmp < 0) ? -1 : 1; // ties to right/top
        } else {
            double cmp = p.y() - n.p.y();
            return (cmp < 0) ? -1 : 1;
        }
    }
}
