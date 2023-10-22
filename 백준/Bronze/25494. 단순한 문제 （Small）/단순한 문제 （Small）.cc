// 단순한 문제 (Small)

#include <iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int testcase, temp_a, temp_b, temp_c;

	cin >> testcase;

	for (int i = 0; i < testcase; i++)
	{
		cin >> temp_a >> temp_b >> temp_c;
		cout << min(min(temp_a, temp_b), temp_c) << endl;
	}
}
