// Торговый центр

#include <iostream>
using namespace std;

int main() {
  int bus_number, result;
  cin >> bus_number;

  result = 200000;
  for (int i = 0; i < bus_number; i++) {
    int a, b;
    cin >> a >> b;
    if (result > a + b)
      result = a + b;
  }

  cout << result << endl;
}
