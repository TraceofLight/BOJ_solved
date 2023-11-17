// Population

#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int line_number;
  cin >> line_number;

  for (int i = 0; i < line_number; i++) {
    int population, time_passed;
    cin >> population >> time_passed;
    population += time_passed / 4;
    population -= time_passed / 7;
    cout << population << endl;
  }
}
