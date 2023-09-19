// 이 얼마나 끔찍하고 무시무시한 수식이니

#include <iostream>
#include <vector>

using namespace std;

string ft_expression_to_num(string target);
string ft_num_to_string(long long number);
long long ft_operation(string expression);
long long ft_calc(long long num1, long long num2, int calc_type);
void ft_throw_madness(void);

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string expression, expression_num, result;
	long long calc_result;

	cin >> expression;
	expression_num = ft_expression_to_num(expression);
	calc_result = ft_operation(expression_num);
	result = ft_num_to_string(calc_result);

	cout << expression_num << endl;
	cout << result << endl;
}

string ft_expression_to_num(string target)
{
	vector<string> number_vector;
	string temp;

	number_vector = {
		"ZERO", "ONE", "TWO",
		"THREE", "FOUR", "FIVE",
		"SIX", "SEVEN", "EIGHT", "NINE",
	};

	for (int i = 0; i < 10; i++)
	{
		while (target.find(number_vector[i]) != string::npos)
		{
			temp.clear();
			temp.push_back('0' + i);
			target.replace(
				target.find(number_vector[i]),
				number_vector[i].size(),
				temp
			);
		}
	}

	return (target);
}

long long ft_operation(string expression)
{
	long long result, now_number;
	int pointer, operation_type;
	bool was_operator;
	string operators, available_char;

	if (!expression.find('='))
		ft_throw_madness();

	result = 0;
	now_number = 0;
	pointer = 0;
	operation_type = 0;
	was_operator = false;
	operators = "+-x/";
	available_char = "0123456789+-x/=";

	while (pointer < (int) expression.size())
	{
		if (available_char.find(expression[pointer]) == string::npos)
			ft_throw_madness();

		if (pointer == (int) expression.size() - 1)
		{
			if (expression[pointer] != '=')
				ft_throw_madness();
			if (was_operator)
				ft_throw_madness();
			else
				result = ft_calc(result, now_number, operation_type);
		}
		else
		{
			if (expression[pointer] == '=')
				ft_throw_madness();
			if (was_operator && operators.find(expression[pointer]) != string::npos)
				ft_throw_madness();
			else
			{
				if (operators.find(expression[pointer]) != string::npos)
				{
					result = ft_calc(result, now_number, operation_type);
					now_number = 0;
					was_operator = true;
					if (expression[pointer] == '+')
						operation_type = 0;
					else if (expression[pointer] == '-')
						operation_type = 1;
					else if (expression[pointer] == 'x')
						operation_type = 2;
					else if (expression[pointer] == '/')
						operation_type = 3;
				}
				else
				{
					was_operator = false;
					now_number *= 10;
					now_number += expression[pointer] - '0';
				}
			}
		}
		pointer++;
	}

	return (result);
}

string ft_num_to_string(long long number)
{
	string result;
	vector<string> number_vector;

	number_vector = {
		"ZERO", "ONE", "TWO",
		"THREE", "FOUR", "FIVE",
		"SIX", "SEVEN", "EIGHT", "NINE",
	};

	if (number < 0)
	{
		result += "-";
		number *= -1;
	}

	if (number < 10)
		result += number_vector[number];
	else
	{
		result += ft_num_to_string(number / 10);
		result += number_vector[number % 10];
	}

	return (result);
}

long long ft_calc(long long num1, long long num2, int calc_type)
{
	if (!calc_type)
		num1 += num2;
	else if (calc_type == 1)
		num1 -= num2;
	else if (calc_type == 2)
		num1 *= num2;
	else if (calc_type == 3)
		num1 /= num2;

	return (num1);
}

void ft_throw_madness(void)
{
	cout << "Madness!" << endl;
	exit (0);
}
