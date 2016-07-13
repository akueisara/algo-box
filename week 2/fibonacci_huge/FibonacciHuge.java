import java.util.*;

public class FibonacciHuge {

    private static long getFibonacciHuge(long n, int m) {
		if (n == 0)
			return 0;

		ArrayList<Integer> fibList= new ArrayList<>();
		ArrayList<Integer> modList = new ArrayList<>();
		
		fibList.add(0, 0);
		fibList.add(1, 1);		
		modList.add(0, 0);
		modList.add(1, 1);
	
		int i=2;
		while(true) {
			fibList.add(i, modList.get(i-1) + modList.get(i-2));
			modList.add(i, fibList.get(i) % m);
			if(modList.get(i-1) == 0 && modList.get(i) == 1)
				break;
			i++;
		}
		int remainder = (int)(n % (i-1)); // The period length is i-1
		return fibList.get(remainder) % m;
    }

    // Examples calculated Pisano numbers:
    // http://willnicholes.com/math/pisano.htm
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        int m = scanner.nextInt();

        System.out.println(getFibonacciHuge(n, m));
    }
}
