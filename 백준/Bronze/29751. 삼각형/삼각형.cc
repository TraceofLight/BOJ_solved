// 삼각형

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	double width, height, area;

	cin >> width >> height;
	area = width * height / 2;

	cout << fixed;
	cout.precision(1);

	cout << area << endl;
}
