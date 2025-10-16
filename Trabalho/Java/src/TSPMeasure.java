import algs4.In;
import algs4.StdOut;

public class TSPMeasure {
    public static void main(String[] args) {
        if (args.length < 1) {
            StdOut.println("Uso: java TSPMeasure <arquivo>");
            return;
        }

        String filename = args[0];
        In in = new In(filename);

        // primeiras duas entradas são dimensões; consumi-las e ignorá-las
        in.readInt();
        in.readInt();

        Tour tour = new Tour(); // usa KdTree por padrão

        while (!in.isEmpty()) {
            double x = in.readDouble();
            double y = in.readDouble();
            Point p = new Point(x, y);
            tour.insertNearest(p);
        }

        StdOut.println("Arquivo: " + filename);
        StdOut.println("Comprimento (vizinho mais próximo): " + tour.length());
    }
}
