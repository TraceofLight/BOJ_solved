// 출석 이벤트

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int coupon, price, result;

	cin >> coupon;
	cin >> price;

	if (coupon >= 20)
		result = min(price * 3 / 4, price - 2000);
	else if (coupon >= 15)
		result = min(price * 9 / 10, price - 2000);
	else if (coupon >= 10)
		result = min(price * 9 / 10, price - 500);
	else if (coupon >= 5)
		result = price - 500;
	else
		result = price;

	if (result < 0)
		cout << 0 << endl;
	else
		cout << result << endl;
}
