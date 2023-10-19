// 출석 이벤트

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int plan_number, temp, total_time;

	cin >> plan_number;
	total_time = 0;

	for (int i = 0; i < plan_number; i++)
	{
		cin >> temp;
		total_time += temp;
		if (i)
			total_time += 8;
	}

	cout << total_time / 24 << " " << total_time % 24 << endl;
}
