// Time to Decompress

#include <iostream>
using namespace std;

int main() {
  int testcase;
  cin >> testcase;
  for (int i = 0; i < testcase; i++) {
    int repeat_num;
    char chr;
    cin >> repeat_num >> chr;
    for (int j = 0; j < repeat_num; j++)
      cout << chr;
    cout << endl;
  }
}
