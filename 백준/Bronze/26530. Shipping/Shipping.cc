// Shipping

#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int datacase;
	cin >> datacase;

	for (int i = 0; i < datacase; i++) {
		int item_number;
		double total_cost;
		cin >> item_number;
		total_cost = 0;

		for (int j = 0; j < item_number; j++) {
			string item_name;
			int item_number;
			double item_cost;
			cin >> item_name >> item_number >> item_cost;

			total_cost += item_cost * item_number;
		}

		cout << "$";
		cout << fixed;
		cout.precision(2);
		cout << total_cost << endl;
	}
}
