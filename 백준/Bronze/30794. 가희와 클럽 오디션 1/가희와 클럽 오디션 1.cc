// 가희와 클럽 오디션 1

#include <iostream>
using namespace std;

int main() {
  int result;
  result = 0;

  int lvl;
  string score;
  cin >> lvl >> score;
  if (score == "bad")
    result = lvl * 200;
  else if (score == "cool")
    result = lvl * 400;
  else if (score == "great")
    result = lvl * 600;
  else if (score == "perfect")
    result = lvl * 1000;

  cout << result << endl;
}
