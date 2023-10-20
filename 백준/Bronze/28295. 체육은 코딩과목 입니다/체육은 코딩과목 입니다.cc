// 체육은 코딩과목 입니다

#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int now_position, temp_order;
	string directions;

	now_position = 0;
	directions = "NESW";

	for (int i = 0; i < 10; i++)
	{
		cin >> temp_order;
		now_position += temp_order;
	}

	cout << directions[now_position % 4] << endl;
}
