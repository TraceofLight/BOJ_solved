// 민주주의

#include <iostream>
using namespace std;

int main() {
  int q_num, person_num, result;

  cin >> q_num >> person_num;
  result = 0;
  for (int i = 0; i < q_num; i++) {
    string temp;
    int vote;

    cin >> temp;
    vote = 0;
    for (char c : temp) {
      if (c == 'O')
        vote++;
      else
        vote--;
    }
    if (vote > 0)
      result++;
  }

  cout << result << endl;
}
