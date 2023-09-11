// 2033년 밈 투표

#include <iostream>
#include <unordered_set>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int testcase;
	bool is_all_meme;
	string temp_string;
	unordered_set<string> meme_set;

	cin >> testcase;
	cin.ignore();
	is_all_meme = true;

	meme_set = {
		"Never gonna give you up",
		"Never gonna let you down",
		"Never gonna run around and desert you",
		"Never gonna make you cry",
		"Never gonna say goodbye",
		"Never gonna tell a lie and hurt you",
		"Never gonna stop",
	};

	for (int i = 0; i < testcase; i++)
	{
		getline(cin, temp_string);
		if (meme_set.find(temp_string) == meme_set.end())
			is_all_meme = false;
	}

	if (is_all_meme)
		cout << "No" << endl;
	else
		cout << "Yes" << endl;
}
