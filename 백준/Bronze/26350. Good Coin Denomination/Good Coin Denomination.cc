// Good Coin Denomination

#include <iostream>
#include <sstream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int testcase;
	cin >> testcase;

	for (int i = 0; i < testcase; i++) {
		int denomination_number;
		int now_denomination;
		bool is_good = true;

		cin >> denomination_number;
		cin.ignore();

		string denomination_info;
		getline(cin, denomination_info);
		cout << "Denominations: " << denomination_info << endl; 
		stringstream denomination_stream(denomination_info);

		for (int j = 0; j < denomination_number; j++) {
			if (!j) denomination_stream >> now_denomination;
			else {
				int next_denomination;
				denomination_stream >> next_denomination;
				if (next_denomination < 2 * now_denomination) {
					is_good = false;
				}
				now_denomination = next_denomination;
			}
		}

		if (is_good) cout << "Good coin denominations!" << endl << endl;
		else cout << "Bad coin denominations!" << endl << endl;
	}
}
