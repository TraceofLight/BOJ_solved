// 빵

#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int store_number, move_time, left_time, result;

	result = 1001;

	cin >> store_number;
	for (int i = 0; i < store_number; i++)
	{
		cin >> move_time >> left_time;
		if (move_time <= left_time)
			result = min(result, left_time);
	}
	
	if (result == 1001)
		cout << -1 << endl;
	else
		cout << result << endl;
}
