import java.util.*;

public class PointsAndSegments {
    
    private static class Segment {
        int x;
        int y;

        public Segment(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "[" + x +
                    ", " + y +
                    ']';
        }
    }

    private static int[] fastCountSegments(int[] starts, int[] ends, int[] points) {
        int[] cnt = new int[points.length];
        TreeSet<Segment> pointsSortedByX = new TreeSet<>(new OrderX());
        for (int i = 0; i < starts.length; i++) {
            pointsSortedByX.add(new Segment(starts[i], ends[i]));
        }
        for (int i = 0; i < points.length; i++) {
            TreeSet<Segment> pointsSortedByY = new TreeSet<>(new OrderY());
            Segment search = new Segment(points[i], points[i]);
            pointsSortedByY.addAll(pointsSortedByX.headSet(search, true));
            cnt[i] = pointsSortedByY.tailSet(search, true).size();
        }
        return cnt;
    }

    private static int[] naiveCountSegments(int[] starts, int[] ends, int[] points) {
        int[] cnt = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            for (int j = 0; j < starts.length; j++) {
                if (starts[j] <= points[i] && points[i] <= ends[j]) {
                    cnt[i]++;
                }
            }
        }
        return cnt;
    }
    
    private static class OrderX implements Comparator<Segment> {
        public int compare(Segment p, Segment q) {
            return Integer.compare(p.x, q.x);
        }
    }

    private static class OrderY implements Comparator<Segment> {
        public int compare(Segment p, Segment q) {
            return Integer.compare(p.y, q.y);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n, m;
        n = scanner.nextInt();
        m = scanner.nextInt();
        int[] starts = new int[n];
        int[] ends = new int[n];
        int[] points = new int[m];
        for (int i = 0; i < n; i++) {
            starts[i] = scanner.nextInt();
            ends[i] = scanner.nextInt();
        }
        for (int i = 0; i < m; i++) {
            points[i] = scanner.nextInt();
        }
        // int[] cnt = naiveCountSegments(starts, ends, points);
        //use fastCountSegments
        int[] cnt = fastCountSegments(starts, ends, points);
        for (int x : cnt) {
            System.out.print(x + " ");
        }
    }
}