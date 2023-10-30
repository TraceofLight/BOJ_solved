// Divide the Cash

#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int team_number, money, total_seperation, temp;
	vector<int> team_info;

	total_seperation = 0;
	cin >> team_number >> money;
	
	for (int i = 0; i < team_number; i++) {
		cin >> temp;
		total_seperation += temp;
		team_info.push_back(temp);
	}

	for (auto iter = team_info.begin(); iter < team_info.end(); ++iter)
		cout << (money / total_seperation) * *iter << endl;
}
