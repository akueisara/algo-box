#include <iostream>
#include <string.h>

int calc_fib(int n) {
	if(n <= 1)
		return n;
	else if(n == 2)
		return 1;
	else {
		int result[n+1];
		memset(result, 0, sizeof(result));
		result[1] = 1;
		result[2] = 1;
		for(int i=3;i<n+1;i++) {
			result[i] = result[i-1] + result[i-2];
		}
		return result[n];
	} 
}

int main() {
    int n = 0;
    std::cin >> n;

    std::cout << calc_fib(n) << '\n';
    return 0;
}
