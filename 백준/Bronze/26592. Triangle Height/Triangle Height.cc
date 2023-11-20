// Triangle Height

#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int homework_amount;
  cin >> homework_amount;

  for (int i = 0; i < homework_amount; i++) {
    double area, base, height;
    cin >> area >> base;
    height = area * 2 / base;
    cout << "The height of the triangle is ";
    cout << fixed;
    cout.precision(2);
    cout << height;
    cout << " units" << endl;
  }
}
