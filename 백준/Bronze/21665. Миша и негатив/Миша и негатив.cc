// Миша и негатив

#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int height, width, result;
	vector<vector<char>> image;
	string temp;

	cin >> height >> width;

	image.resize(height);
	for (int i = 0; i < height; i++)
	{
		cin >> temp;
		image[i].resize(width);
		for (int j = 0; j < width; j++)
		{
			if (temp[j] == 'W')
				image[i][j] = 'B';
			else
				image[i][j] = 'W';
		}
	}

	result = 0;

	for (int i = 0; i < height; i++)
	{
		cin >> temp;
		for (int j = 0; j < width; j++)
		{
			if (temp[j] != image[i][j])
				result++;
		}
	}

	cout << result << endl;

	return (0);
}
