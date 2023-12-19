// Final Price

#include <iostream>
using namespace std;

int main() {
  int line_number, result, temp;

  cin >> line_number;
  result = 0;
  for (int i = 0; i < line_number; i++) {
    cin >> temp;
    result += temp;
  }

  cout << result << endl;
}
