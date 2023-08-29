// Äpplen och päron

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int apple, pear;

	cin >> apple >> pear;
	apple *= 7;
	pear *= 13;

	if (apple < pear)
		cout << "Petra" << endl;
	else if (apple > pear)
		cout << "Axel" << endl;
	else
		cout << "lika" << endl;

	return (0);
}
