// Простая задача

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int quiz_number, conditional_statement, loop;

	cin >> quiz_number;
	
	for (int i = 0; i < quiz_number; i++)
	{
		cin >> conditional_statement >> loop;

		if (
			conditional_statement + loop <= 3 
				&& conditional_statement < 3
					&& loop < 3
		)
			cout << "Yes" << endl;
		else
			cout << "No" << endl;
	}
}
