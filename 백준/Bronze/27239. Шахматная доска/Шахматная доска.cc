// Шахматная доска

#include <iostream>
using namespace std;

int main() {
  int target_block;
  cin >> target_block;
  target_block--;

  string row_num = "12345678";
  string col_num = "abcdefgh";

  cout << col_num[target_block % 8];
  cout << row_num[target_block / 8];
  cout << endl;
}
