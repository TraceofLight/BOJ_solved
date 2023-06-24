# solved.ac

from math import floor


def round(target_number: float) -> int:
    if target_number >= floor(target_number) + 0.5:
        return floor(target_number) + 1
    else:
        return floor(target_number)


opinion_number = int(input())

if not opinion_number:
    print(0)

else:
    scores = []
    for _ in range(opinion_number):
        scores.append(int(input()))
    scores.sort()

    exception_number = round(opinion_number * 0.15)

    sum_score = 0
    for i in range(exception_number, opinion_number - exception_number):
        sum_score += scores[i]

    result = round(sum_score / (opinion_number - 2 * exception_number))
    print(result)
