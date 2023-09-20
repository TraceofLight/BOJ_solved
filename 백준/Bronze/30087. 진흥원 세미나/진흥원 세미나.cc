// 진흥원 세미나

#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int class_number;
	string temp_input;
	unordered_map<string, string> class_map;

	class_map.insert(make_pair("Algorithm", "204"));
	class_map.insert(make_pair("DataAnalysis", "207"));
	class_map.insert(make_pair("ArtificialIntelligence", "302"));
	class_map.insert(make_pair("CyberSecurity", "B101"));
	class_map.insert(make_pair("Network", "303"));
	class_map.insert(make_pair("Startup", "501"));
	class_map.insert(make_pair("TestStrategy", "105"));

	cin >> class_number;

	for (int i = 0; i < class_number; i++)
	{
		cin.ignore();
		cin >> temp_input;
		cout << class_map.find(temp_input) -> second << endl;
	}
}
