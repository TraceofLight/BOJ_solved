// Zagubiona litera

#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  string alphabets;
  alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  int sum_alpha = 0;
  for (int i = 0; i < alphabets.size(); i++) {
    sum_alpha += alphabets[i];
  }

  string input_string;
  cin >> input_string;
  for (int i = 0; i < input_string.size(); i++) {
    sum_alpha -= input_string[i];
  }

  cout << alphabets[sum_alpha - 'A'] << endl;
}
