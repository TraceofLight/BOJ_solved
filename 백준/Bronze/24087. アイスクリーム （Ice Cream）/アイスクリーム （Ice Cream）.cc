// アイスクリーム (Ice Cream)

#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int total_height, height_a, height_b, result;

    cin >> total_height;
    cin >> height_a;
    cin >> height_b;

    result = 250;

    total_height -= height_a;
    if (total_height > 0)
    {
        result += 100 * (total_height / height_b);
        if (total_height % height_b)
            result += 100;
    }

    cout << result << endl;
}
