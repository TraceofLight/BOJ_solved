// Boiling Water

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int temp, result;

	cin >> temp;
	result = temp * 5 - 400;
	cout << result << endl;

	if (result < 100)
		cout << 1 << endl;
	else if (result > 100)
		cout << -1 << endl;
	else
		cout << 0 << endl;

	return (0);
}
