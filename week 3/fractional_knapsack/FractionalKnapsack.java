import java.util.*;

public class FractionalKnapsack {
	private static int get_best_idx(ArrayList<Double> ratios) {
		double best = 0;
		int best_idx = 0;

		for (int i = 0; i < ratios.size(); i++) {
			if (ratios.get(i) > best) {
				best = ratios.get(i);
				best_idx = i;
			}
		}
		return best_idx;
	}
	
    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        double value = 0;
        //write your code here
		ArrayList<Integer> valuelist = new ArrayList<Integer>();
		for (int i : values) 
			valuelist.add(i);
		
		ArrayList<Double> weightlist = new ArrayList<Double>();
		for (double i : weights) 
			weightlist.add(i);
		
		ArrayList<Double> ratios = new ArrayList<Double>();
		for(int i=0;i<valuelist.size();i++) {
		  ratios.add((double)valuelist.get(i)/weightlist.get(i));
        }
		
		while (capacity > 0) {
			int best_idx = get_best_idx(ratios);
			if (weightlist.get(best_idx) > 0) {
				double a = Math.min((double)capacity, (double)weightlist.get(best_idx));
				double ratio = (double) valuelist.get(best_idx) / (double) weightlist.get(best_idx);
				value += a * ratio;
				weightlist.set(best_idx, weightlist.get(best_idx) - a);
				capacity -= a;
			}
			if (weightlist.get(best_idx) == 0) {
				weightlist.remove(best_idx);
				valuelist.remove(best_idx);
				ratios.remove(best_idx);;
			}
		}
		
		return value;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
            weights[i] = scanner.nextInt();
        }
        System.out.println(getOptimalValue(capacity, values, weights));
    }
} 
