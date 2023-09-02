// Checkers

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    long long a, b;

	cin >> a >> b;

    if (a < b) 
		cout << a + 1;
    else
		cout << b;

	return (0);
}
