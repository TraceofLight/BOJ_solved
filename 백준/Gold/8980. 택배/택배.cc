// 택배

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Parcel {
  int start;
  int end;
  int total_box;

  Parcel(int s, int e, int box)
      : start(s), end(e), total_box(box) {}

  Parcel(Parcel &&other) noexcept
      : start(other.start),
        end(other.end),
        total_box(other.total_box) {
  }

  Parcel &operator=(Parcel &&other) noexcept {
    if (this != &other) {
      start = other.start;
      end = other.end;
      total_box = other.total_box;
    }
    return *this;
  }
};

struct Compare {
  bool operator()(const Parcel &first, const Parcel &second) {
    return first.end < second.end;
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

  vector<Parcel> parcel_vector;
  int start, end, parcel_box;
  for (int i = 0; i < query_number; i++) {
    cin >> start >> end >> parcel_box;
    Parcel input_parcel_info = Parcel(start, end, parcel_box);
    parcel_vector.push_back(std::move(input_parcel_info));
  }
  sort(parcel_vector.begin(), parcel_vector.end(), Compare());

  vector<int> capacity_arr(town_number, truck_capacity);
  int result = 0;

  for (Parcel &each_parcel : parcel_vector) {
    int max_load =
        FindMaxLoad(capacity_arr, each_parcel.start, each_parcel.end);
    int now_load = min(max_load, each_parcel.total_box);
    result += now_load;
    UpdateLoad(capacity_arr,
               each_parcel.start,
               each_parcel.end,
               now_load);
  }

  cout << result << endl;
}
