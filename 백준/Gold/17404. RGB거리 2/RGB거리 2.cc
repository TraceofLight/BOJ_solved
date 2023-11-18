// RGB 거리 2

#include <iostream>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int result, house_number;
  cin >> house_number;

  int cost_info[house_number][3];
  for (int i = 0; i < house_number; i++) {
    for (int j = 0; j < 3; j++) {
      cin >> cost_info[i][j];
    }
  }

  int dp[house_number][3];
  result = 2000000;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (i != j) dp[0][j] = 2000000;
      else dp[0][j] = cost_info[0][j];
    }

    for (int j = 1; j < house_number; j++) {
      dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + cost_info[j][0];
      dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + cost_info[j][1];
      dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + cost_info[j][2];
    }

    if (i == 0)
      result =
          min(result, min(dp[house_number - 1][1], dp[house_number - 1][2]));
    else if (i == 1)
      result =
          min(result, min(dp[house_number - 1][0], dp[house_number - 1][2]));
    else if (i == 2)
      result =
          min(result, min(dp[house_number - 1][0], dp[house_number - 1][1]));
  }
  cout << result << endl;
}
