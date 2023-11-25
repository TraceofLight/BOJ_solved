// 택배

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Parcel {
  int start;
  int end;
  int weight;
  int total_box;

  Parcel(int s, int e, int box)
      : start(s), end(e), total_box(box) {
    weight = end - start;
  }
};

struct Compare {
  bool operator()(const Parcel &first, const Parcel &second) {
    return first.weight > second.weight;
  }
};

int FindMaxLoad(vector<int> &target, int start, int end) {
  int min_empty_capacity = 20000;
  for (int i = start; i < end; i++) {
    min_empty_capacity = min(min_empty_capacity, target[i]);
  }
  return min_empty_capacity;
}

void UpdateLoad(vector<int> &target, int start, int end, int value) {
  for (int i = start; i < end; i++) {
    target[i] -= value;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int town_number, truck_capacity;
  cin >> town_number >> truck_capacity;
  int query_number;
  cin >> query_number;

  priority_queue<Parcel, vector<Parcel>, Compare> parcel_pq;
  int start, end, parcel_box;
  for (int i = 0; i < query_number; i++) {
    cin >> start >> end >> parcel_box;
    parcel_pq.push(Parcel(start, end, parcel_box));
  }

  vector<int> capacity_arr(town_number + 1, truck_capacity);
  int result = 0;

  while (!parcel_pq.empty()) {
    int max_load = FindMaxLoad(capacity_arr, parcel_pq.top().start, parcel_pq.top().end);
    int now_load = min(max_load, parcel_pq.top().total_box);
    result += now_load;
    UpdateLoad(capacity_arr, parcel_pq.top().start, parcel_pq.top().end, now_load);
    parcel_pq.pop();
  }
  cout << result << endl;
}
