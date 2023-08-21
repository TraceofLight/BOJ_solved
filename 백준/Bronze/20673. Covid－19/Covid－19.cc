#include <iostream>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int new_case, average;

	cin >> new_case;
	cin >> average;

	if (new_case <= 50 && average <= 10)
		cout <<	"White" << "\n";
	else if (average > 30)
		cout << "Red" << "\n";
	else
		cout << "Yellow" << "\n";

	return (0);
}
