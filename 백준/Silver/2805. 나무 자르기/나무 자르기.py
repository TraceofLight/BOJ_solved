import sys

n, m = list(map(int,sys.stdin.readline().split()))
woods_raw = list(map(int,sys.stdin.readline().split()))

woods = sorted(woods_raw)

def binarySearch(val, list, start, end) :
    result = 0
    if end == start :
        for element in list :
            result += ((element - end) + abs(element - end)) / 2
        if result >= val :
            return end
        else :
            return False
    elif end - start == 1 :
        for i in range(2) :
            for element in list :
                result += ((element - (end - i)) + abs(element - (end - i))) / 2
                if result >= val :
                    return end - i
        return False
    else :
        mid = (end - start) // 2
        for element in list :
            result += ((element - (start + mid)) + abs(element - (start + mid))) / 2
        if result >= val :
            return start + mid
        elif result < val :
            return binarySearch(val, list, start, start + mid - 1)

result = binarySearch(m, woods, 0, woods[-1])
result_before = binarySearch(m, woods, result, woods[-1])

while True :
    if result_before == result : 
        break
    else :
        result = binarySearch(m, woods, result_before, woods[-1])
        result_before = binarySearch(m, woods, result, woods[-1])

print(result)