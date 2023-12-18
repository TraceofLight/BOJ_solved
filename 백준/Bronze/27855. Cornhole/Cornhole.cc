// Cornhole

#include <iostream>
using namespace std;

int main() {
  int h1, b1, h2, b2, result1, result2;

  cin >> h1 >> b1;
  cin >> h2 >> b2;

  result1 = 3 * h1 + b1;
  result2 = 3 * h2 + b2;

  if (result1 > result2)
    cout << "1 " << result1 - result2 << endl;
  else if (result1 < result2)
    cout << "2 " << result2 - result1 << endl;
  else
    cout << "NO SCORE" << endl;
}
