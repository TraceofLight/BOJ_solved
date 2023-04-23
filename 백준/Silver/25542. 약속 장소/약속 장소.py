# 약속 장소

import sys

input = sys.stdin.readline


def is_similar(checker: str, target: str) -> bool:
    
    length = len(checker)
    counter = 0

    for idx in range(length):

        if checker[idx] != target[idx]:
            counter += 1

    if counter <= 1:
        return True
    else:
        return False


store_number, name_length = map(int, input().split())
name_list = []
first_checker = True

for _ in range(store_number):
    each_name = list(input().rstrip('\n'))

    if first_checker:
        target_name = each_name
        first_checker = False

    else:
        name_list.append(each_name)

result_set = set()

for idx in range(name_length):
    for alpha in range(65, 91):
        temp = target_name[:]
        temp[idx] = chr(alpha)
        result_set.add(''.join(temp))

while result_set and name_list:

    now_check_name = name_list.pop()
    remove_target = set()

    for each_result in result_set:
        if not is_similar(now_check_name, each_result):
            remove_target.add(each_result)

    for each_target in remove_target:
        result_set.remove(each_target)

if not result_set:
    print('CALL FRIEND')

else:
    print(result_set.pop())
