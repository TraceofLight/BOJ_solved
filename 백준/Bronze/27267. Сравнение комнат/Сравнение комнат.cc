// Сравнение комнат

#include <iostream>
using namespace std;

int main() {
  int a, b, c, d;

  cin >> a >> b >> c >> d;
  if (a * b > c * d)
    cout << "M" << endl;
  else if (a * b < c * d)
    cout << "P" << endl;
  else
    cout << "E" << endl;
}
