# 그대로 출력하기

# input을 받는 동안 계속 반복
while True:

    # input을 줄바꿈 없이 출력
    try:
        string = input()
        print(string)

    # EOF 에러가 발생하면 종료
    except EOFError:
        break
