// Area

#include <iostream>
using namespace std;

int main() {
  int area_case, result;

  result = 0;
  cin >> area_case;

  for (int i = 0; i < area_case; i++) {
    int a, b;
    cin >> a >> b;
    if (a * b > result)
      result = a * b;
  }

  cout << result << endl;
}
