// 移動 (Moving)

#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	int x, y, z;

	cin >> x;
	cin >> y;
	cin >> z;

	if (x + y > z)
		cout << 0 << endl;
	else
		cout << 1 << endl;
}
