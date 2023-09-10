// 브실이와 친구가 되고 싶어 🤸‍♀️

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int min_solve, max_solve, solve_number, diff, range_start, range_end;

	cin >> min_solve >> max_solve;
	cin >> solve_number >> diff;

	range_start = solve_number - diff;
	range_end = solve_number + diff;

	if (range_end < min_solve || range_start > max_solve)
		cout << "IMPOSSIBLE" << endl;
	else 
	{
		if (range_start < min_solve)
			range_start = min_solve;
		if (range_end > max_solve)
			range_end = max_solve;
		cout << range_end - range_start + 1 << endl;
	}

	return (0);
}
