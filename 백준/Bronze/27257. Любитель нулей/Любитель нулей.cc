// Любитель нулей

#include <iostream>
using namespace std;

int main() {
  int number;
  cin >> number;

  while (!(number % 10))
    number /= 10;

  int result = 0;
  while (number) {
    if (!(number % 10))
      result++;
    number /= 10;
  }

  cout << result << endl;
}
