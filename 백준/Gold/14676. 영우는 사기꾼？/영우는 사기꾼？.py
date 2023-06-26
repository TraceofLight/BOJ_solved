# 영우는 사기꾼?

import sys

input = sys.stdin.readline

building_number, relation_number, game_info_number = map(int, input().split())

prebuild_arr = [0 for _ in range(building_number + 1)]
build_arr = [0 for _ in range(building_number + 1)]
prerequisites = [set() for _ in range(building_number + 1)]

for _ in range(relation_number):
    pre_build, next_build = map(int, input().split())
    prebuild_arr[next_build] += 1
    prerequisites[pre_build].add(next_build)

is_lier = False

for _ in range(game_info_number):
    query_type, target_building = map(int, input().split())

    if query_type == 1:
        if prebuild_arr[target_building]:
            is_lier = True
        else:
            build_arr[target_building] += 1

            if build_arr[target_building] == 1:
                for each_next_build in prerequisites[target_building]:
                    prebuild_arr[each_next_build] -= 1

    elif query_type == 2:
        if build_arr[target_building] == 0:
            is_lier = True

        else:
            build_arr[target_building] -= 1

            # 제거 후 없다면 해당 빌딩 건설을 필요로 하는 집합 재카운팅
            if not build_arr[target_building]:
                for each_next_build in prerequisites[target_building]:
                    prebuild_arr[each_next_build] += 1

if is_lier:
    print("Lier!")
else:
    print("King-God-Emperor")
