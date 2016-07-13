import java.util.*;

public class LCM {
  private static long gcd(long a, long b) {
	if (b == 0)
		return a;
	return gcd(b, a%b);
  }
	
  private static long lcm(long a, long b) {
    //write your code here
    return a * b / gcd(a,b);
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    long a = scanner.nextLong();
    long b = scanner.nextLong();

    System.out.println(lcm(a, b));
  }
}
