# 정보섬의 대중교통

walk, bus, subway = map(int, input().split())

if bus < subway:
    print('Bus')
elif bus > subway:
    print('Subway')
else:
    print('Anything')
