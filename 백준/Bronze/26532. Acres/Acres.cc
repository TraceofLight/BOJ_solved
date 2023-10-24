// Acres

#include <iostream>
#include <cmath>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int width, height;
	double result;

	cin >> width >> height;
	result = width * height / (4840 * 5.0);

	cout << ceil(result) << endl;
}
