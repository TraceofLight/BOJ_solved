// 페이지 세기

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int				total_page, seperator, start, end, result;
	string			temp, each_range;
	vector<string>	line_info;
	vector<bool>	print_info;
	vector<int>		result_vector;

	while (true)
	{
		cin >> total_page;

		if (!total_page)
			break ;
		else
		{
			print_info.assign(1500, false);
			cin.ignore();
			getline(cin, temp);
			stringstream range_stream(temp);

			while (getline(range_stream, each_range, ','))
			{
				if (each_range.find('-') == string::npos)
				{
					if (each_range.length() < 5 && stoi(each_range) <= 1000)
						print_info[stoi(each_range)] = true;
				}
				else
				{
					seperator = each_range.find('-');
					if (each_range.substr(0, seperator).length() < 5
						&& stoi(each_range.substr(0, seperator)) <= 1000)
						start = stoi(each_range.substr(0, seperator));
					else
						start = 1001;
					if (each_range.substr(seperator + 1, each_range.size()).length() < 5 
						&& stoi(each_range.substr(seperator + 1, each_range.size())) <= 1000)
						end = stoi(each_range.substr(seperator + 1, each_range.size()));
					else
						end = 1001;
					if (start <= end)
					{
						for (int i = start; i <= end; i++)
						{
							if (i <= total_page)
								print_info[i] = true;
						}
					}
				}
			}

			result = 0;
			for (int i = 1; i <= total_page; i++)
			{
				if (print_info[i])
					result++;
			}
			result_vector.push_back(result);
		}
	}

	for (int i = 0; i < (int) result_vector.size(); i++)
		cout << result_vector[i] << endl;

	return (0);
}
