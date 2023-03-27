# 인공지능 시계

import sys

input = sys.stdin.readline

hour, minute, second = map(int, input().split())
total_second = hour * 3600 + minute * 60 + second

cooking_time = int(input())
total_second += cooking_time
total_second %= 3600 * 24

end_hour = total_second // 3600
total_second %= 3600

end_minute = total_second // 60
total_second %= 60

end_second = total_second

print(end_hour, end_minute, end_second)
