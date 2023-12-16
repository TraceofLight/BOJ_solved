// Sun and Moon

#include <iostream>
using namespace std;

int main() {
  int ds, ys, dm, ym, year_sun, year_moon;
  cin >> ds >> ys;
  cin >> dm >> ym;

  year_sun = ys - ds;
  year_moon = ym - dm;
  while (year_sun != year_moon) {
    if (year_sun > year_moon)
      year_moon += ym;
    else
      year_sun += ys;
  }

  cout << year_sun << endl;
}
