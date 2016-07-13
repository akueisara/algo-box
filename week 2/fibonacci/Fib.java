import java.util.Scanner;

public class Fib {
  private static long calc_fib(int n) {

	if(n <= 1)
		return n;
	else if(n == 2)
		return 1;
	else {
		int [] result = new int[n+1];
		result[1] = 1;
		result[2] = 1;
		for(int i=3;i<n+1;i++) {
			result[i] = result[i-1] + result[i-2];
		}
		return result[n];
	}
  }

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    System.out.println(calc_fib(n));
  }
}
