// 연세워터파크

#include <iostream>
#include <queue>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int bridge_number, max_jump;
  cin >> bridge_number >> max_jump;

  long long result;
  int bridge_info[bridge_number];
  for (int i = 0; i < bridge_number; i++) {
    cin >> bridge_info[i];
  }

  auto compare_pair =
      [](const pair<long long, int> &first,
         const pair<long long, int> &second) {
        return (first.first < second.first);
      };

  priority_queue<pair<long long, int>,
                 vector<pair<long long, int>>,
                 decltype(compare_pair)> max_priority(compare_pair);

  pair<long long, int> now_pair;
  now_pair.first = bridge_info[0];
  now_pair.second = 0;
  max_priority.push(now_pair);
  result = bridge_info[0];

  for (int i = 1; i < max_jump; i++) {
    now_pair.first = max((long long) bridge_info[i],
                         max_priority.top().first + bridge_info[i]);
    now_pair.second = i;
    max_priority.push(now_pair);
    if (result < max_priority.top().first) result = max_priority.top().first;
  }

  for (int i = max_jump; i < bridge_number; i++) {
    while (!max_priority.empty()
        && (i - max_priority.top().second > max_jump))
      max_priority.pop();
    now_pair.first = max((long long) bridge_info[i],
                         max_priority.top().first + bridge_info[i]);
    now_pair.second = i;
    max_priority.push(now_pair);
    if (result < max_priority.top().first) result = max_priority.top().first;
  }

  cout << result << endl;
}
