import java.util.*;

public class GCD {
  private static int gcd(int a, int b) {
    // int current_gcd = 1;
    // for(int d = 2; d <= a && d <= b; ++d) {
    // }

    // return current_gcd;
	if (b == 0)
		return a;
	return gcd(b, a%b);
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(gcd(a, b));
  }
}
