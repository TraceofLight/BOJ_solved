// 사장님 도박은 재미로 하셔야 합니다

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int result, temp;

	result = 0;
	while (true)
	{
		cin >> temp;
		if (temp == -1)
			break ;
		else
			result += temp;
	}

	cout << result << endl;
}
