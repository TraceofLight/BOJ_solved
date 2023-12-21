// Chili Peppers

#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
  int pepper_number, result;
  unordered_map<string, int> shu_map;

  shu_map.insert({"Poblano", 1500});
  shu_map.insert({"Mirasol", 6000});
  shu_map.insert({"Serrano", 15500});
  shu_map.insert({"Cayenne", 40000});
  shu_map.insert({"Thai", 75000});
  shu_map.insert({"Habanero", 125000});

  cin >> pepper_number;
  result = 0;
  for (int i = 0; i < pepper_number; i++) {
    string temp;
    cin >> temp;
    result += shu_map[temp];
  }

  cout << result << endl;
}
