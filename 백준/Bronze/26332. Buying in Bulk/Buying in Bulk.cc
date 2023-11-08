// Buying in Bulk

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int item_number, item_amount, price;

    cin >> item_number;

    for (int i = 0; i < item_number; i++) {
        cin >> item_amount >> price;
        cout << item_amount << " " << price << endl;
        if (item_amount == 1) cout << price << endl;
        else {
            int calc_result = price + max(price - 2, 0) * (item_amount - 1);
            cout << calc_result << endl;
        }
    }
}
