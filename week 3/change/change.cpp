#include <iostream>

int get_change(int n) {
  //write your code here
  int result = 0;
  result += n/10;
  n = n % 10;
  result += n/5;
  n = n % 5;
  n = n + result;
  return n;
}

int main() {
  int n;
  std::cin >> n;
  std::cout << get_change(n) << '\n';
}