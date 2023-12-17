// 특별한 작은 분수

#include <iostream>
using namespace std;

int main() {
  int fountain, seconds;

  cin >> fountain >> seconds;
  while (seconds)
  {
    if (fountain % 2)
      fountain = (2 * fountain) ^ 6;
    else
      fountain = (fountain / 2) ^ 6;
    seconds--;
  }

  cout << fountain << endl;
}
