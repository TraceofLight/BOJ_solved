// No Brainer

#include <iostream>
using namespace std;

int main() {
  int testcase;
  cin >> testcase;

  for (int i = 0; i < testcase; i++) {
    int eat, need;
    cin >> eat >> need;

    if (eat >= need)
      cout << "MMM BRAINS" << endl;
    else
      cout << "NO BRAINS" << endl;
  }
}
