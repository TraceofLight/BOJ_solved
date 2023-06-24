# 평균은 넘겠지


from math import floor


def round_four_decimal(target_number: float) -> float:
    check_number = target_number * 1000

    if check_number >= floor(check_number) + 0.5:
        return f"{(floor(check_number) + 1) / 1000:.3f}"
    else:
        return f"{(floor(check_number)) / 1000:.3f}"


testcase = int(input())
output = []

for _ in range(testcase):
    student_number, *scores = map(int, input().split())
    average = sum(scores) / student_number
    count = 0
    for each_score in scores:
        if each_score > average:
            count += 1

    result = round_four_decimal(count / student_number * 100)

    output.append(f"{result}%")

for result in output:
    print(result)
