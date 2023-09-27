// Lucky 7

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int number, remainder;
	bool have_seven;

	cin >> number;
	remainder = number % 7;

	have_seven = false;
	while (number)
	{
		if (number % 10 == 7)
		{
			have_seven = true;
			break;
		}
		number /= 10;
	}

	if (!have_seven && remainder)
		cout << 0 << endl;
	else if (!have_seven && !remainder)
		cout << 1 << endl;
	else if (have_seven && remainder)
		cout << 2 << endl;
	else if (have_seven && !remainder)
		cout << 3 << endl;
}
