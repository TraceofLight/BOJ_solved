// Betting

#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	double p, result1, result2;
	cin >> p;

	result1 = 100 / p;
	result2 = 100 / (100 - p);

	cout << fixed;
	cout.precision(4);

	cout << result1 << endl;
	cout << result2 << endl;
}
