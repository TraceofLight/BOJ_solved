// 3의 배수

#include <iostream>
#include <vector>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<char> input_number;
	string input_line;
	int now_sum, sum_digit, temp, count_logic;

	getline(cin, input_line);

	for (char c : input_line)
		input_number.push_back(c);

	if (input_number.size() == 1)
	{
		count_logic = 0;
		now_sum = input_number[0] - '0';
	}
	else
	{
		count_logic = 1;
		now_sum = 0;

		for (char each_digit : input_number)
			now_sum += each_digit - '0';

		while (now_sum >= 10)
		{
			sum_digit = 0;
			temp = now_sum;
			while (temp)
			{
				sum_digit += temp % 10;
				temp /= 10;
			}
			now_sum = sum_digit;
			count_logic += 1;
		}
	}

	cout << count_logic << "\n";
	if (!(now_sum % 3))
		cout << "YES\n";
	else
		cout << "NO\n";

	return (0);
}
