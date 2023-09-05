// SMS from MCHS

#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int today_temp, today_wind, tomorrow_temp, tomorrow_wind;

	cin >> today_temp >> today_wind;
	cin >> tomorrow_temp >> tomorrow_wind;

	if (tomorrow_temp < 0 && tomorrow_wind >= 10)
		cout << "A storm warning for tomorrow! Be careful and stay home if possible!" << endl;
	else
	{
		if (today_temp > tomorrow_temp)
			cout << "MCHS warns! Low temperature is expected tomorrow." << endl; 
		else if (today_wind < tomorrow_wind)
			cout << "MCHS warns! Strong wind is expected tomorrow." << endl;
		else
			cout << "No message" << endl;
	}

	return (0);
}
