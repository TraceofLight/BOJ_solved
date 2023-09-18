// 스위트콘 가격 구하기

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int price, result;

	cin >> price;
	result = price / 11 * 10;

	cout << result << endl;
}
