// Дневник Гравити Фолз

#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int width, height, a_width, a_height, max_alpha, result;
  double n;
  cin >> width >> height;
  cin >> n >> a_width >> a_height;

  max_alpha = (width / a_width) * (height / a_height);
  if (!max_alpha)
    cout << -1 << endl;
  else {
    result = ceil(n / max_alpha);
    cout << result << endl;
  }
}
