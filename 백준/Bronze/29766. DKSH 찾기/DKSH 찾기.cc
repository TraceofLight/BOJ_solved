// DKSH 찾기

#include <iostream>
using namespace std;

int main() {
  int result;
  string input_string;

  result = 0;
  cin >> input_string;
  for (int i = 0; i < input_string.size(); i++) {
    if (input_string.substr(i, 4) == "DKSH")
      result++;
  }
  cout << result << endl;
}
