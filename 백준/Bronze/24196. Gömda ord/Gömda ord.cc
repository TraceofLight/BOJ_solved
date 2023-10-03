// Gömda ord

#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string input_string;
    int count;

    cin >> input_string;
    count = 0;

    for (int i = 0; i < (int) input_string.size(); i++)
    {
        if (i == (int) input_string.size())
        {
            cout << input_string[i] << endl;
            break ;
        }
        else if (count)
        {
            count--;
            continue ;
        }
        count = input_string[i] - 'A';
        cout << input_string[i];
    }
}
