// Планеты двух измерений

#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int n, m, max_result;
  cin >> n >> m;

  if (n == m)
    max_result = n + m;
  else
    max_result = min(n, m) * 2 + 1;

  cout << max_result << endl;
}
