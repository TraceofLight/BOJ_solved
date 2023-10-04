// ГРАДИНА

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int w1, h1, w2, h2, result;

	cin >> w1 >> h1 >> w2 >> h2;

	result = (h1 + h2 + max(w1, w2)) * 2 + 4;
	cout << result << endl;
}
