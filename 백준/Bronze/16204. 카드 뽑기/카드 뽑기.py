# 카드 뽑기

n, m, k = map(int, input().split())
card = m
left_card = n - m
back = k
left_back = n - k

result = min(card, back) + min(left_card, left_back)
print(result)
