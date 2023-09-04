// 졸려

#include <iostream>
#include <vector>

using namespace std;

vector<int> flicker_action(int target_length, int count);

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int flicker_number;
    string result_string, init_string;
    vector<char> string_vector;
    vector<int> idx_vector;

    cin >> flicker_number;
    cin.ignore();
    getline(cin, result_string);

    for (int i = 0; i < (int) result_string.length(); i++)
        string_vector.push_back(result_string[i]);
    

    idx_vector = flicker_action(result_string.length(), flicker_number);
    init_string.resize(result_string.length());

    for (int i = 0; i < (int) result_string.length(); i++)
        init_string[idx_vector[i]] = result_string[i];

    cout << init_string << endl;
    return (0);
}

vector<int> flicker_action(int target_length, int count)
{
    vector<int> result, temp_vector, start_vector;
	int cycle;

    for (int i = 0; i < target_length; i++)
        result.push_back(i);

	start_vector = result;
	cycle = 1;

    for (int i = 1; i <= target_length - 1; i++)
    {
		temp_vector.clear();
		temp_vector.resize(target_length);
        for (int j = 0; j < target_length; j++)
        {
			if (!(j % 2))
				temp_vector[j] = result[j / 2];
			else
				temp_vector[j] = result[target_length - 1 - (j / 2)];
        }

		if (start_vector == temp_vector)
		{
			cycle = i;
			break ;
		}
		else
			result = temp_vector;
    }

	result = start_vector;

    for (int i = 0; i < (count % cycle); i++)
    {
		temp_vector.clear();
		temp_vector.resize(target_length);
        for (int j = 0; j < target_length; j++)
        {
			if (!(j % 2))
				temp_vector[j] = result[j / 2];
			else
				temp_vector[j] = result[target_length - 1 - (j / 2)];
        }

		result = temp_vector;
    }

    return (result);
}
