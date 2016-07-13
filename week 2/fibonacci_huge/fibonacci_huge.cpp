#include <iostream>
#include <vector>

using std::vector;

long long get_fibonaccihuge(long long n, long long m) {
  //write your code here
	if(n == 0)
		return 0;
  
	vector<long> fib(n+1);
	vector<long> mod(m+1);
	
	fib[0] = 0;
	fib[1] = 1;
	mod[0] = 0;
	mod[1] = 1;

	int i=2;
	while(true) {
		fib[i] = mod[i-1] + mod[i-2];
		mod[i] = fib[i] % m;
		if(mod[i-1] == 0 && mod[i] == 1)
			break;
		i++;
	}
	int remainder = (int)(n % (i-1)); // The period length is i-1
	return fib[remainder] % m;
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonaccihuge(n, m) << '\n';
}
