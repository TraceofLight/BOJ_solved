// Pizza

#include <iostream>
#include <cmath>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  const double pi = 3.14159265358979;

  int data_amount;
  cin >> data_amount;

  for (int i = 0; i < data_amount; i++) {
    double piece_area, piece_price, whole_radius, whole_price;
    cin >> piece_area >> piece_price;
    cin >> whole_radius >> whole_price;

    double piece_cost_effectiveness, whole_cost_effectiveness;
    piece_cost_effectiveness = piece_area / piece_price;
    whole_cost_effectiveness = pow(whole_radius, 2) * pi / whole_price;

    if (piece_cost_effectiveness > whole_cost_effectiveness)
      cout << "Slice of pizza" << endl;
    else
      cout << "Whole pizza" << endl;
  }
}
