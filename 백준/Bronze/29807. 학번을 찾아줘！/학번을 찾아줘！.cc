// 학번을 찾아줘!

#include <iostream>
using namespace std;

int main() {
  int subject_number, kor, math, eng, sci, second_lang;
  long long result;

  cin >> subject_number;
  kor = 0;
  math = 0;
  eng = 0;
  sci = 0;
  second_lang = 0;

  if (subject_number >= 1)
    cin >> kor;
  if (subject_number >= 2)
    cin >> math;
  if (subject_number >= 3)
    cin >> eng;
  if (subject_number >= 4)
    cin >> sci;
  if (subject_number >= 5)
    cin >> second_lang;

  result = 0;
  if (kor > eng)
    result += (kor - eng) * 508;
  else
    result += (eng - kor) * 108;
  if (math > sci)
    result += (math - sci) * 212;
  else
    result += (sci - math) * 305;
  if (second_lang)
    result += second_lang * 707;
  result *= 4763;

  cout << result << endl;
}
