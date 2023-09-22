// 計算 (Calculation)

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a, b, sum, sub;
	
	cin >> a >> b;
	sum = a + b;
	sub = a - b;
	if (sum >= sub)
	{
		cout << sum << endl;
		cout << sub << endl;
	}
	else
	{
		cout << sub << endl;
		cout << sum << endl;
	}
}
