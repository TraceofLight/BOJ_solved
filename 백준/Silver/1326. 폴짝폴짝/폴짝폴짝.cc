// 폴짝폴짝

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

typedef struct s_frog
{
	int	index;
	int move_count;
} t_frog;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int bridge_length, start, end;
	string temp, each_info;
	vector<int> bridge_info, visit_log;
	vector<t_frog> progress_stack;
	stringstream bridge_stream;
	t_frog start_frog, now_frog, next_frog;

	cin >> bridge_length;
	visit_log.resize(bridge_length, 2147483647);

	cin.ignore();
	getline(cin, temp);
	bridge_stream = stringstream(temp);

	while (bridge_stream >> each_info)
		bridge_info.push_back(stoi(each_info));

	cin >> start >> end;

	start--;
	end--;
	start_frog.index = start;
	start_frog.move_count = 0;
	visit_log[start] = 0;

	progress_stack.push_back(start_frog);

	while (!progress_stack.empty())
	{
		now_frog = progress_stack.front();

		if (now_frog.index <= bridge_length)
		{
			for (int i = now_frog.index; 0 <= i && i < bridge_length; i += bridge_info[now_frog.index])
			{
				if (now_frog.move_count + 1 < visit_log[i])
				{
					next_frog.index = i;
					next_frog.move_count = now_frog.move_count + 1;
					visit_log[i] = now_frog.move_count + 1;
					progress_stack.push_back(next_frog);
				}
			}
			for (int i = now_frog.index; 0 <= i && i < bridge_length; i -= bridge_info[now_frog.index])
			{
				if (now_frog.move_count + 1 < visit_log[i])
				{
					next_frog.index = i;
					next_frog.move_count = now_frog.move_count + 1;
					visit_log[i] = now_frog.move_count + 1;
					progress_stack.push_back(next_frog);
				}
			}
		}

		progress_stack.erase(progress_stack.begin());
	}

	if (visit_log[end] == 2147483647)
		cout << -1 << endl;
	else
		cout << visit_log[end] << endl;

	return (0);
}
