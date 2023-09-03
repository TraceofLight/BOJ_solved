// Bank Transfer

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int money;
	double charge;

	cin >> money;
	charge = money * 0.01 + 25;

	if (charge < 100)
		cout << 100 << endl;
	else if (charge > 2000)
		cout << 2000 << endl;
	else
	{
		cout << fixed;
		cout.precision(3);
		cout << charge << endl;
	}

	return (0);
}
