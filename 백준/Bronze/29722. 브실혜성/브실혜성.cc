// 브실혜성

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	char spliter;
	int now_year, now_month, now_date, orbit_cycle, result, \
		next_year, next_month, next_date;

	cin >> now_year >> spliter >> now_month >> spliter >> now_date;
	cin >> orbit_cycle;

	result = 360 * (now_year - 1) + 30 * (now_month - 1) + now_date + orbit_cycle;
	next_year = result / 360 + 1;
	next_month = (result % 360) / 30 + 1;
	next_date = result % 30;

	if (!next_date)
	{
		next_month--;
		next_date += 30;
	}

	cout << next_year << spliter;
	if (next_month < 10)
		cout << "0" << next_month << spliter;
	else
		cout << next_month << spliter;
	if (next_date < 10)
		cout << "0" << next_date << endl;
	else
		cout << next_date << endl;

	return (0);
}
