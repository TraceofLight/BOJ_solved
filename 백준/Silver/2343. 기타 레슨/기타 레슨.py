# 기타 레슨

import sys

# 비디오 갯수, 디스크 갯수 input
video_number, disk_number = map(int, sys.stdin.readline().split())
# 비디오 길이 정보 input
video_list = list(map(int, sys.stdin.readline().split()))

# 크기의 범위는 동영상 중 가장 긴 길이부터 전체 합한 길이까지
min_volume = max(video_list)
max_volume = sum(video_list)


# 블루레이 볼륨을 넣었을 때 디스크 갯수를 반환하는 함수
def check_volume(check_list:list, volume:int):
    disk_counter = 0
    now_video_volume = 0
    for each_video in check_list:
        # 디스크 갯수 확인
        if now_video_volume == volume:
            disk_counter += 1
            now_video_volume = 0
        elif now_video_volume < volume:
            if now_video_volume + each_video > volume:
                disk_counter += 1
                now_video_volume = each_video
            elif now_video_volume + each_video == volume:
                disk_counter += 1
                now_video_volume = 0
            else:
                now_video_volume += each_video
    # 정상 연산이 진행된 경우 잔여 강의가 남았다면 디스크 +1
    if now_video_volume != 0:
        disk_counter += 1
    return disk_counter

# 디스크의 부피 최소점을 이분탐색을 통하여 진행할 수 있도록 하는 함수 선언
def search_volume(target_number, start_volume, end_volume, element_list):
    start_point = start_volume
    end_point = end_volume
    while (end_point - start_point):
        mid_point = (start_point + end_point) // 2
        result_amount = check_volume(element_list, mid_point)
        if result_amount > target_number:
            start_point = mid_point + 1
        elif result_amount <= target_number:
            end_point = mid_point
    return end_point


# 함수를 호출하여 과정 진행
result = search_volume(disk_number, min_volume, max_volume, video_list)

# 결과 출력
print(result)
