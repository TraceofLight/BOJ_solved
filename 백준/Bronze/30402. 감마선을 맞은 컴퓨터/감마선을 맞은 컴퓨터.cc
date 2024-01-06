// 감마선을 맞은 컴퓨터

#include <iostream>
#include <array>
using namespace std;

int main() {
  int result;
  array<string, 3> cat_arr = {"chunbae", "nabi", "yeongcheol"};

  result = 0;
  for (int i = 0; i < 15; i++) {
    string temp;
    cin >> temp;
    for (char c : temp) {
      if (c == 'w')
        result = 0;
      if (c == 'b')
        result = 1;
      if (c == 'g')
        result = 2;
    }
  }

  cout << cat_arr.at(result) << endl;
}
