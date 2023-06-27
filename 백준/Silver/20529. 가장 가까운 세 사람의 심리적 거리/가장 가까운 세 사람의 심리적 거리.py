# 가장 가까운 세 사람의 심리적 거리

import sys
from itertools import product, combinations

input = sys.stdin.readline


def psychological_distance(target_1: str, target_2: str) -> int:
    '''
    MBTI를 비교하고 심리적 거리를 반환하는 함수
    '''
    result = 0

    for i in range(4):
        if target_1[i] != target_2[i]:
            result += 1

    return result


mbti_list = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 
             'ISTP', 'ISFP', 'INFP', 'INTP', 
             'ESTP', 'ESFP', 'ENFP', 'ENTP', 
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

distance_dict = dict()
for each_combination in product(mbti_list, mbti_list):
    mbti1, mbti2 = each_combination
    distance = psychological_distance(mbti1, mbti2)
    distance_dict[mbti1 + mbti2] = distance
    distance_dict[mbti2 + mbti1] = distance

testcase = int(input())
output = []

for _ in range(testcase):

    student_number = int(input())
    mbti_list = list(input().split())

    min_result = 20
    for each_mbti_couple in combinations(mbti_list, 3):
        
        mbti_a, mbti_b, mbti_c = each_mbti_couple
        dist_result = (
            distance_dict.get(mbti_a + mbti_b) 
            + distance_dict.get(mbti_b + mbti_c) 
            + distance_dict.get(mbti_c + mbti_a)
        )
        
        if min_result > dist_result:
            min_result = dist_result

        if not min_result:
            break

    output.append(min_result)

for result in output:
    print(result)
