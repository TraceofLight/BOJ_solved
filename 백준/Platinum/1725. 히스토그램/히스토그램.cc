// 히스토그램

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int FindMiddleMaxArea(vector<int> &data_vector,
                      int start,
                      int end,
                      int front_max_area,
                      int back_max_area) {
  int max_area = max(front_max_area, back_max_area);
  int mid = (start + end) / 2;
  int width = 1;
  int min_height;
  int start_pointer;
  int end_pointer;
  if (data_vector[mid] > data_vector[mid + 1]) {
    min_height = data_vector[mid + 1];
    start_pointer = mid + 1;
    end_pointer = mid + 1;
  } else {
    min_height = data_vector[mid];
    start_pointer = mid;
    end_pointer = mid;
  }

  while (start <= start_pointer && end_pointer <= end) {
    if (start == start_pointer && end_pointer == end)
      break;
    else if (start_pointer == start
        || data_vector[start_pointer - 1] <= data_vector[end_pointer + 1])
      end_pointer++;
    else if (end_pointer == end
        || data_vector[start_pointer - 1] > data_vector[end_pointer + 1])
      start_pointer--;
    width++;
    min_height = min(min(min_height, data_vector[start_pointer]),
                     data_vector[end_pointer]);
    if (min_height * width > max_area)
      max_area = min_height * width;
  }

  return max_area;
}

int SetDataOnTree(vector<int> &tree_vector,
                  vector<int> &data_vector,
                  int start,
                  int end,
                  int now_node) {
  if (start == end) {
    tree_vector[now_node] = data_vector[start];
  } else {
    int mid = (start + end) / 2;
    int front_max_area =
        SetDataOnTree(tree_vector,
                      data_vector,
                      start,
                      mid,
                      2 * now_node + 1);
    int back_max_area =
        SetDataOnTree(tree_vector,
                      data_vector,
                      mid + 1,
                      end,
                      2 * now_node + 2);

    int max_area = FindMiddleMaxArea(data_vector,
                                     start,
                                     end,
                                     front_max_area,
                                     back_max_area);

    tree_vector[now_node] = max_area;
  }

  return tree_vector[now_node];
}

int FindMaxArea(vector<int> &array_info) {
  int tree_size =
      static_cast<int>(pow(2,
                           static_cast<int>(ceil(log2(array_info.size()))
                               + 1)));
  vector<int> tree_area_vector(tree_size);
  int max_area =
      SetDataOnTree(tree_area_vector,
                    array_info,
                    0,
                    static_cast<int>(array_info.size()) - 1,
                    0);

  return max_area;
}

int main() {
  int height_number;
  cin >> height_number;

  vector<int> height_info(height_number);
  for (int i = 0; i < height_number; i++)
    cin >> height_info[i];

  int result = FindMaxArea(height_info);

  cout << result << endl;
}
