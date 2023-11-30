// Rain Diary

#include <iostream>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;

  if (n <= 7)
    cout << m + 7 << endl;
  else
    cout << n - 7 << endl;
}
