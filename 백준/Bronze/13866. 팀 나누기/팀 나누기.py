# 팀 나누기

skill_list = list(map(int, input().split()))
skill_list.sort()
result = abs((skill_list[0] + skill_list[3]) - (skill_list[1] + skill_list[2]))

print(result)
