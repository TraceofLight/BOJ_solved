// 준영이의 등급

#include <iostream>
using namespace std;

int main() {
  int total_student, subject_number;
  cin >> total_student >> subject_number;

  for (int i = 0; i < subject_number; i++) {
    int temp;
    cin >> temp;
    temp *= 100;
    temp /= total_student;
    if (temp <= 4) cout << 1;
    else if (temp <= 11) cout << 2;
    else if (temp <= 23) cout << 3;
    else if (temp <= 40) cout << 4;
    else if (temp <= 60) cout << 5;
    else if (temp <= 77) cout << 6;
    else if (temp <= 89) cout << 7;
    else if (temp <= 96) cout << 8;
    else cout << 9;
    if (i != subject_number - 1) cout << " ";
  }
  cout << endl;
}
