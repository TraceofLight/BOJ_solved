// ПЧЕЛИЧКАТА МАЯ

#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a, b, c, avg, result;

	cin >> a >> b >> c;
	avg = (a + b + c) / 3;
	result = 0;

	if (a != avg)
		result += abs(a - avg);
	if (c != avg)
		result += abs(c - avg);

	cout << result << endl;
}
