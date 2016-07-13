#include <iostream>
#include <vector>

using std::vector;

int get_fibonacci_last_digit(int n) {
  //write your code here
  vector<int> result(n+1);
  result[0] = 0;
  result[1] = 1;
  for(int i=2; i< result.size();i++) {
	  result[i] = (result[i - 1] + result[i - 2]) % 10;
  }
  return result[n];
}

int main() {
  int n;
  std::cin >> n;
  int c = get_fibonacci_last_digit(n);
  std::cout << c << '\n';
}
