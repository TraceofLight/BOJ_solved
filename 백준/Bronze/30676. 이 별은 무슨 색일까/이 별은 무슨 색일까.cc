// 이 별은 무슨 색일까

#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int wave_length;
  cin >> wave_length;

  if (620 <= wave_length && wave_length <= 780) cout << "Red" << endl;
  else if (590 <= wave_length && wave_length < 620) cout << "Orange" << endl;
  else if (570 <= wave_length && wave_length < 590) cout << "Yellow" << endl;
  else if (495 <= wave_length && wave_length < 570) cout << "Green" << endl;
  else if (450 <= wave_length && wave_length < 495) cout << "Blue" << endl;
  else if (425 <= wave_length && wave_length < 450) cout << "Indigo" << endl;
  else if (380 <= wave_length && wave_length < 425) cout << "Violet" << endl;
}
