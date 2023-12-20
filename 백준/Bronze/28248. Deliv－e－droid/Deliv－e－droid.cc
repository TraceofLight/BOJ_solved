// Deliv-e-droid

#include <iostream>
using namespace std;

int main() {
  int package, crash, score;
  cin >> package;
  cin >> crash;

  score = 0;
  score += package * 50;
  score -= crash * 10;
  if (package > crash)
    score += 500;

  cout << score << endl;
}
