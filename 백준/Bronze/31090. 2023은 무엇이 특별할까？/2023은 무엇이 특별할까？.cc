// 2023은 무엇이 특별할까?

#include <iostream>
using namespace std;

int main() {
  int testcase;

  cin >> testcase;
  for (int i = 0; i < testcase; i++) {
    int temp;
    cin >> temp;

    if (!((temp + 1) % (temp % 100)))
      cout << "Good" << endl;
    else
      cout << "Bye" << endl;
  }
}
