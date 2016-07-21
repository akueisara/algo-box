import java.util.*;

// class SegmentsComparator implements Comparator<CoveringSegments.Segment>{
 
	// @Override
	// public int compare(CoveringSegments.Segment s1, CoveringSegments.Segment s2) {
		// return s1.end - s2.end;
	// }
// }

public class CoveringSegments {

    private static int[] optimalPoints(Segment[] segments) {
        int[] points = new int[2 * segments.length];
		// Arrays.sort(segments, new SegmentsComparator());	
		Arrays.sort(segments, new Comparator<Segment>() {
			@Override
			public int compare(Segment s1, Segment s2) {
				return Integer.compare(s1.end, s2.end);
			}
		});
		int current = segments[0].end;
		points[0] = current;
		int j = 1;
        for (int i = 0; i < segments.length; i++) {
			if (current < segments[i].start || current > segments[i].end) {
				current = segments[i].end;
				points[j] = current;
				j++;
			}
        }
        int[] result = new int[j];
        for(int i=0; i<j; i++) {
        	result[i] = points[i];
        }
        return result;
    }

    public static class Segment {
        int start, end;

        Segment(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Segment[] segments = new Segment[n];
        for (int i = 0; i < n; i++) {
            int start, end;
            start = scanner.nextInt();
            end = scanner.nextInt();
            segments[i] = new Segment(start, end);
        }
        int[] points = optimalPoints(segments);
        System.out.println(points.length);
        for (int point : points) {
            System.out.print(point + " ");
        }
    }
}