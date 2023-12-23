// Previous Level

#include <iostream>
using namespace std;

int main() {
  int lvl_num, temp;
  cin >> lvl_num;
  for (int i = 0; i < lvl_num; i++) {
    cin >> temp;
    if (temp == 300) cout << "1";
    else if (275 <= temp && temp < 300) cout << "2";
    else if (250 <= temp && temp < 275) cout << "3";
    else cout << "4";
    if (i != lvl_num - 1) cout << " ";
  }
  cout << endl;
}
