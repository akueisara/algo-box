#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

int edit_distance(const string &str1, const string &str2) {
	int n = str1.size();
	int m = str2.size();
	vector<vector<int> > d(n + 1, vector<int>(m + 1, 0));
	for(int i = 0; i <= n; ++i) {
        d[i][0] = i;
    }
    for(int i = 0; i <= m; ++i) {
        d[0][i] = i;
    }
	int cost = 0;
	for(int i = 1; i <= n; ++i) {
		for(int j = 1; j <= m; ++j) {
			if(str1[i-1] == str2[j-1])
				cost = 0;
			else
				cost = 1;
			d[i][j] = std::min(std::min(d[i-1][j],d[i][j-1]) + 1, d[i-1][j-1] + cost);
		}
	}
	return d[n][m];
}

int main() {
  string str1;
  string str2;
  std::cin >> str1 >> str2;
  std::cout << edit_distance(str1, str2) << std::endl;
  return 0;
}
