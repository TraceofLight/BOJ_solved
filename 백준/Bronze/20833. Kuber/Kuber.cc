#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int result, target_number;

	result = 0;
	cin >> target_number;
	for (int i = 1; i <= target_number; i++)
		result += pow(i, 3);
	cout << result << "\n";

	return (0);
}
