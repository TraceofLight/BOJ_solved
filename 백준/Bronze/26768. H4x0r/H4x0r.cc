// H4x0r

#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  string input_string;
  cin >> input_string;

  for (char each_char : input_string) {
    if (each_char == 'a')
      cout << '4';
    else if (each_char == 'e')
      cout << '3';
    else if (each_char == 'i')
      cout << '1';
    else if (each_char == 'o')
      cout << '0';
    else if (each_char == 's')
      cout << '5';
    else
      cout << each_char;
  }
  cout << endl;
}
