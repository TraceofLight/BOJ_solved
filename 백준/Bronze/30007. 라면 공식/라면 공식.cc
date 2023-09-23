// 라면 공식

#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int ramen_number, temp_a, temp_b, temp_x, temp_result;

    cin >> ramen_number;

    for (int i = 0; i < ramen_number; i++)
    {
        cin >> temp_a >> temp_b >> temp_x;
        temp_result = temp_a * (temp_x - 1) + temp_b;
        cout << temp_result << endl;
    }
}
