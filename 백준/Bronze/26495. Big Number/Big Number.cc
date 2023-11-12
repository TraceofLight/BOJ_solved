// Big Number

#include <iostream>
using namespace std;

void print_block(std::string::iterator iter) {
	if (*iter == '0') {
		cout << "0000" << endl;
		cout << "0  0" << endl;
		cout << "0  0" << endl;
		cout << "0  0" << endl;
		cout << "0000" << endl;
	} else if (*iter == '1') {
		cout << "   1" << endl;
		cout << "   1" << endl;
		cout << "   1" << endl;
		cout << "   1" << endl;
		cout << "   1" << endl;
	} else if (*iter == '2') {
		cout << "2222" << endl;
		cout << "   2" << endl;
		cout << "2222" << endl;
		cout << "2" << endl;
		cout << "2222" << endl;
	} else if (*iter == '3') {
		cout << "3333" << endl;
		cout << "   3" << endl;
		cout << "3333" << endl;
		cout << "   3" << endl;
		cout << "3333" << endl;
	} else if (*iter == '4') {
		cout << "4  4" << endl;
		cout << "4  4" << endl;
		cout << "4444" << endl;
		cout << "   4" << endl;
		cout << "   4" << endl;
	} else if (*iter == '5') {
		cout << "5555" << endl;
		cout << "5" << endl;
		cout << "5555" << endl;
		cout << "   5" << endl;
		cout << "5555" << endl;
	} else if (*iter == '6') {
		cout << "6666" << endl;
		cout << "6" << endl;
		cout << "6666" << endl;
		cout << "6  6" << endl;
		cout << "6666" << endl;
	} else if (*iter == '7') {
		cout << "7777" << endl;
		cout << "   7" << endl;
		cout << "   7" << endl;
		cout << "   7" << endl;
		cout << "   7" << endl;
	} else if (*iter == '8') {
		cout << "8888" << endl;
		cout << "8  8" << endl;
		cout << "8888" << endl;
		cout << "8  8" << endl;
		cout << "8888" << endl;
	} else if (*iter == '9') {
		cout << "9999" << endl;
		cout << "9  9" << endl;
		cout << "9999" << endl;
		cout << "   9" << endl;
		cout << "   9" << endl;
	}
	cout << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	string input_number;
	cin >> input_number;

	for (auto iter = input_number.begin(); iter < input_number.end(); ++iter) {
		print_block(iter);
	}
}
