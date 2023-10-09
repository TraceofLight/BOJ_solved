// ЧАСОВНИК

#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t1, m1, t2, m2, start, end;

    cin >> t1 >> m1 >> t2 >> m2;
    start = t1 * 60 + m1;
    end = t2 * 60 + m2;

    if (start == end)
        cout << 0 << " " << 0 << endl;
    else if (start > end)
    {
        end += 1440;
        cout << end - start << " " << (end - start) / 30 << endl; 
    }
    else
        cout << end - start << " " << (end - start) / 30 << endl; 
}
