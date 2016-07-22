#include <iostream>
#include <cassert>
#include <vector>
#include <math.h> 
#include <algorithm> 

using namespace std;

int binary_search(const vector<int> &a, int x) {
  int low = 0, high = (int)a.size() - 1; 
  while(low <= high) {
	  int mid = low + (high - low)/2;
	  if (x == a[mid])
		  return mid;
	  else if (x < a[mid])
		  high = mid - 1;
	  else
		  low = mid + 1;
  }
  return -1;
}

int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    cin >> a[i];
  }
  int m;
  cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    cin >> b[i];
  }
  sort(a.begin(), a.end()); 
  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    // std::cout << linear_search(a, b[i]) << ' ';
	cout << binary_search(a, b[i]) << ' ';
  }
}