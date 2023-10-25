// 지폐 세기

#include <iostream>

using std::ios_base;
using std::cin;
using std::cout;
using std::string;
using std::endl;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int testcase, sum, temp1, temp2;

	cin >> testcase;
	sum = 0;

	for (int i = 0; i < testcase; i++) {
		cin >> temp1 >> temp2;
		if (temp1 == 136 || temp2 == 136)
			sum += 1000;
		else if (temp1 == 142 || temp2 == 142)
			sum += 5000;
		else if (temp1 == 148 || temp2 == 148)
			sum += 10000;
		else if (temp1 == 154 || temp2 == 154)
			sum += 50000;
	}

	cout << sum << endl;
}
