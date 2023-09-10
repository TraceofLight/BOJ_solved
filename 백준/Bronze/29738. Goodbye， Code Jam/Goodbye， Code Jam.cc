// Goodbye, Code Jam

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int testcase, now_rank;

	cin >> testcase;

	for (int i = 1; i <= testcase; i++)
	{
		cin >> now_rank;

		if (now_rank <= 25)
			cout << "Case #" << i << ": World Finals" << endl;
		else if (now_rank <= 1000)
			cout << "Case #" << i << ": Round 3" << endl;
		else if (now_rank <= 4500)
			cout << "Case #" << i << ": Round 2" << endl;
		else
			cout << "Case #" << i << ": Round 1" << endl;
	}

	return (0);
}
