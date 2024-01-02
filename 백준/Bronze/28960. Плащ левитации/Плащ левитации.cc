// Плащ левитации

#include <iostream>
using namespace std;

int main() {
  int rope_height, rope_length, a, b;
  bool result;

  cin >> rope_height >> rope_length >> a >> b;
  result = false;

  if (rope_height * 2 >= a && rope_length >= b)
    result = true;
  else if (rope_height * 2 >= b && rope_length >= a)
    result = true;

  if (result)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
}
