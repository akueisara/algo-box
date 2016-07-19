import java.util.Scanner;

public class Change {
    private static int getChange(int n) {
        //write your code here
		int result = 0;
		result += n/10;
		n = n % 10;
		result += n/5;
		n = n % 5;
		n = n + result;
        return n;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(getChange(n));

    }
}