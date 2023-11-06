// Lots of Liquid

#include <iostream>
#include <cmath>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int liquid_number;
	double total_liquid, temp;

	cin >> liquid_number;
	total_liquid = 0;

	for (int i = 0; i < liquid_number; i++) {
		cin >> temp;
		total_liquid += pow(temp, 3);
	}

	cout << fixed;
	cout.precision(6);
	cout << pow(total_liquid, 1.0/3) << endl;
}
