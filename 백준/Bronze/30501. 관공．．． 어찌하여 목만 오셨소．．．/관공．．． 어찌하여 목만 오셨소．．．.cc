// 관공... 어찌하여 목만 오셨소...

#include <iostream>
using namespace std;

int main() {
  int person_number;
  string result;

  cin >> person_number;
  for (int i = 0; i < person_number; i++) {
    string temp;
    cin >> temp;
    if (temp.find('S') != string::npos)
      result = temp;
  }
  cout << result << endl;
}
