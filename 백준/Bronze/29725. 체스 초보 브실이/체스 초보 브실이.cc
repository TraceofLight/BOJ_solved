// 체스 초보 브실이

#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
  unordered_map<char, int> score_map;
  int result;

  score_map.insert(pair<char, int>('.', 0));
  score_map.insert(pair<char, int>('k', 0));
  score_map.insert(pair<char, int>('p', -1));
  score_map.insert(pair<char, int>('n', -3));
  score_map.insert(pair<char, int>('b', -3));
  score_map.insert(pair<char, int>('r', -5));
  score_map.insert(pair<char, int>('q', -9));
  score_map.insert(pair<char, int>('K', 0));
  score_map.insert(pair<char, int>('P', 1));
  score_map.insert(pair<char, int>('N', 3));
  score_map.insert(pair<char, int>('B', 3));
  score_map.insert(pair<char, int>('R', 5));
  score_map.insert(pair<char, int>('Q', 9));

  result = 0;
  for (int i = 0; i < 8; i++) {
    string temp;
    cin >> temp;
    for (char c : temp)
      result += score_map[c];
  }
  cout << result << endl;
}
