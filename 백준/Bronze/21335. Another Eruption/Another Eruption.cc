// Another Eruption

#include <iostream>
#include <cmath>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long long area;
	double radius, result;

	const double pi = acos(-1);
	cin >> area;

	radius = sqrt(area / pi);
	result = 2 * radius * pi;

	cout << fixed;
	cout.precision(6);
	cout << result << endl;
	cout.unsetf(ios::fixed);

	return (0);
}
