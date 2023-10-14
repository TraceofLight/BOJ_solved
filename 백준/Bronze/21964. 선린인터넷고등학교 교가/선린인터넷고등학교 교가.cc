// 선린인터넷고등학교 교가

#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int     length;
    string  input_string;

    cin >> length;
    cin >> input_string;

    for (int i = length - 5; i < length; i++)
    {
        if (i >= 0)
            cout << input_string[i];
    }
    cout << endl;
}
