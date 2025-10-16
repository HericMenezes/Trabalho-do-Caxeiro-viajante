import algs4.*;
import java.util.HashMap;

public class Tour {

    private static class Node {
        private Point point;
        private Node next;
    }

    private Node start;
    private int count;
    private final boolean useKdTree;
    private KdTree kdTree;
    // Mapa auxiliar para localizar o Node diretamente a partir do Point2D retornado
    // pela KdTree
    private HashMap<Point2D, Node> kdIndex;

    public Tour() {
        this(true);
    }

    public Tour(boolean useKdTree) {
        this.useKdTree = useKdTree;
        this.start = null;
        this.count = 0;
        if (useKdTree) {
            kdTree = new KdTree(); // Inicializa a KdTree
            kdIndex = new HashMap<>();
        }
    }

    public Tour(Point a, Point b, Point c, Point d) {
        this();
        insertNearestNaive(a);
        insertNearestNaive(b);
        insertNearestNaive(c);
        insertNearestNaive(d);
    }

    public int size() {
        return count;
    }

    public double length() {
        if (start == null || start.next == start)
            return 0.0;

        double total = 0.0;
        Node current = start;
        do {
            total += current.point.distanceTo(current.next.point);
            current = current.next;
        } while (current != start);
        return total;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        if (start == null)
            return "(Tour vazio)";

        Node current = start;
        do {
            sb.append(current.point.toString()).append("\n");
            current = current.next;
        } while (current != start);

        return sb.toString();
    }

    public void draw() {
        if (start == null || start.next == start)
            return;

        Node current = start;
        do {
            current.point.drawTo(current.next.point);
            current = current.next;
        } while (current != start);
    }

    public void insertNearest(Point p) {
        if (useKdTree) {
            insertNearestKd(p); // ainda não implementado
        } else {
            insertNearestNaive(p);
        }
    }

    public void insertNearestNaive(Point p) {
        // Para o tour vazio, devo verifico e inicio um novo
        if (start == null) {
            start = new Node(); // Crio um novo Nó
            start.point = p; // Adiciono a coordenada P ao Nó
            start.next = start; // Aponta para si mesmo para mantermos o tour circular
            count++; // Incrementei um P então adiciona mais um ao contador
            return; // Retorno, pois já adicionei o ponto
        }

        Node current = start; // O começo do tour que vai passear por todos os pontos dentro do tour
        Node nearest = start; // Ponto mais próximo, vai guardar o ponto mais próximo encontrado por current

        double minDistance = p.distanceTo(start.point); // Distância mínima do ponto atual, sem que tenha verificado
        // (rodado no loop) todos os pontos.

        do {
            double dist = p.distanceTo(current.point); // Distância do Próximo ponto (current) para o ponto P que quero
            // inserir

            if (dist < minDistance) { // Se o proximo ponto for menor que a distância mínima (o ponto atual) ele
                // realiza a troca do minDistance e do nearest
                minDistance = dist; // Atualiza a distância para a distancia do próximo ponto
                nearest = current; // Atualiza para o próximo ponto
            }

            current = current.next; // Ponteiro avança para o próximo nó, em busca do ponto mais próximo
        } while (current != start);// Current irá visitar todos os pontos até voltar para o ponto de inicio o
        // (start)

        // Insere um novo Nó após o nearest (vizinho mais próximo) for encontrado
        Node newNode = new Node(); // Cria um novo nó para a coordenada P
        newNode.point = p; // Adiciona o ponto P ao novo nó
        newNode.next = nearest.next; // Sincroniza o próximo do novo nó para o próximo do nearest
        nearest.next = newNode; // O próximo do nearest agora aponta para o novo nó (A -> P)
        count++; // Incrementa o contador de pontos
    }

    public void insertNearestKd(Point p) {
        if (start == null) {
            start = new Node();
            start.point = p;
            start.next = start;
            count++;

            if (useKdTree) {
                kdTree = new KdTree();
                kdIndex = new HashMap<>();
                Point2D first = new Point2D(p.x, p.y);
                kdTree.insert(first);
                kdIndex.put(first, start);
            }
            return;
        }

        // Encontra o ponto mais próximo usando a KdTree
        Point2D nearestKd = kdTree.nearest(new Point2D(p.x, p.y));

        // Localiza o Node correspondente no tour (O(1) via índice)
        Node nearestNode = (kdIndex != null) ? kdIndex.get(nearestKd) : null;
        if (nearestNode == null) {
            // Fallback de segurança (não deve ocorrer): faz varredura
            Node current = start;
            do {
                if (current.point.x == nearestKd.x() && current.point.y == nearestKd.y()) {
                    nearestNode = current;
                    break;
                }
                current = current.next;
            } while (current != start);
            if (nearestNode == null)
                throw new RuntimeException("Erro: nearestNode não encontrado no Tour");
        }

        // Insere após o nearestNode
        Node newNode = new Node();
        newNode.point = p;
        newNode.next = nearestNode.next;
        nearestNode.next = newNode;
        count++;

        // Insere o ponto na KdTree e atualiza o índice
        Point2D inserted = new Point2D(p.x, p.y);
        kdTree.insert(inserted);
        if (kdIndex != null)
            kdIndex.put(inserted, newNode);
    }

    // Método de teste (opcional)
    public static void main(String[] args) {
        Tour tour = new Tour(true);
        tour.insertNearest(new Point(1.0, 1.0));
        tour.insertNearest(new Point(1.0, 4.0));
        tour.insertNearest(new Point(4.0, 4.0));
        tour.insertNearest(new Point(4.0, 1.0));

        StdOut.println("# de pontos = " + tour.size());
        StdOut.println("Comprimento = " + tour.length());
        StdOut.println(tour);

        StdDraw.setXscale(0, 6);
        StdDraw.setYscale(0, 6);
        tour.draw();
    }
}