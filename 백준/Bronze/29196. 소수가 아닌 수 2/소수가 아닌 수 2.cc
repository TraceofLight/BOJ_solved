#include <iostream>
#include <cmath>
using namespace std;

int	main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	double p, q, input_number, calc_result, limit_number;

	cin >> input_number;
	p = 1;
	q = 1;
	limit_number = pow(10, -6);

	while (p <= pow(10, 9) && q <= pow(10, 9))
	{
		calc_result = p / q;
		if (abs(calc_result - input_number) <= limit_number)
			break;
		else
		{
			if (calc_result > input_number)
				q += 1;
			else
				p += 1;
		}
	}

	if (p > pow(10, 9) || q > pow(10, 9))
		cout << "NO\n";
	else
	{
		cout << "YES\n";
		cout << p << " " << q << "\n";
	}

	return (0);
}
