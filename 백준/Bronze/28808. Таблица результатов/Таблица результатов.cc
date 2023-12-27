// Таблица результатов

#include <iostream>
using namespace std;

int main() {
  int case_num, try_count, result;

  cin >> case_num >> try_count;
  result = 0;

  for (int i = 0; i < case_num; i++) {
    char temp;
    bool is_solved = false;
    for (int j = 0; j < try_count; j++) {
      cin >> temp;
      if (temp == '+')
        is_solved = true;
    }
    if (is_solved)
      result++;
  }

  cout << result << endl;
}
