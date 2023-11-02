// 경사로

#include <iostream>
#include <vector>
using namespace std;

int CheckVertical(vector<vector<int> >& target, int col_num, int runway_size) {
    int count, last_floor, pass_count;
    vector<int> vertical_line;

    vertical_line.reserve(target.size());
    for (const auto& row: target) {
        vertical_line.push_back(row[col_num]);
    }

    last_floor = -1;
    count = 1;
    pass_count = 0;

    for (auto iter = vertical_line.begin(); iter < vertical_line.end(); ++iter) {
        if (last_floor < 0) last_floor = *iter;
        else if (pass_count) {
            pass_count--;
            continue;
        }
        else {
            if (last_floor != *iter) {
                if (abs(last_floor - *iter) > 1 || (last_floor < *iter && count < runway_size)) return (0);
                else if (last_floor > *iter) {
                    for (int i = 0; i < runway_size; i++) {
                        if (iter + i == vertical_line.end() + 1 || *iter != *(iter + i)) return (0);
                    }
                    pass_count += runway_size - 1;
                    count = 0;
                } else {
                    count = 1;
                }
                last_floor = *iter;
            } else count++;
        }
    }

    return (1);
}

int CheckHorizontal(vector<int>& target, int runway_size) {
    int count, last_floor, pass_count;

    last_floor = -1;
    count = 1;
    pass_count = 0;

    for (auto iter = target.begin(); iter < target.end(); ++iter) {
        if (last_floor < 0) last_floor = *iter;
        else if (pass_count) {
            pass_count--;
            continue;
        }
        else {
            if (last_floor != *iter) {
                if (abs(last_floor - *iter) > 1 || (last_floor < *iter && count < runway_size)) return (0);
                else if (last_floor > *iter) {
                    for (int i = 0; i < runway_size; i++) {
                        if (iter + i == target.end() + 1 || *iter != *(iter + i)) return (0);
                    }
                    pass_count += runway_size - 1;
                    count = 0;
                } else {
                    count = 1;
                }
                last_floor = *iter;
            } else count++;
        }
    }

    return (1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int size, runway, result;
    cin >> size >> runway;

    vector<vector<int> > map(size, vector<int>(size));
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) cin >> map[i][j];
    }

    result = 0;
    for (int i = 0; i < size; i++) {
        result += CheckHorizontal(map[i], runway);
        result += CheckVertical(map, i, runway);
    }

    cout << result << endl;
}
