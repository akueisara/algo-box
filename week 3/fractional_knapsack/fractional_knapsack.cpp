#include <iostream>
#include <vector>

using std::vector;
using std::min;

int get_best_idx(vector<double>& ratios) {
  double best = 0;
  int best_idx = 0;

  for (int i = 0; i < ratios.size(); i++) {
    if (ratios[i] > best) {
      best = ratios[i];
      best_idx = i;
    }
  }
  return best_idx;
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;
  // write your code here
  vector<double> ratios(weights.size());
  for(int i=0;i<weights.size();i++) {
    ratios[i] = (double)values[i]/weights[i];
  }
  
  while (capacity > 0) {
    int best_idx = get_best_idx(ratios);
    if (weights[best_idx] > 0) {
      double a = min((double)capacity, (double)weights[best_idx]);
      double ratio = (double) values[best_idx] / (double) weights[best_idx];
      value += a * ratio;
      weights[best_idx] -= a;
	  capacity -= a;
      if (weights[best_idx] == 0) {
        weights.erase(weights.begin() + best_idx);
        values.erase(values.begin() + best_idx);
		ratios.erase(ratios.begin() + best_idx);
      }
    }
  }
  
  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
