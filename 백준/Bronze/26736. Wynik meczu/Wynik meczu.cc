// Wynik meczu

#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  string memo;
  cin >> memo;

  int a_score, b_score;
  a_score = 0;
  b_score = 0;
  for (char each_goal : memo) {
    if (each_goal == 'A')
      a_score++;
    else
      b_score++;
  }

  cout << a_score << " : " << b_score << endl;
}
