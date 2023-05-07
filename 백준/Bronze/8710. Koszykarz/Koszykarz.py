# Koszykarz

now_height, need_height, add_height = map(int, input().split())

counter = 0
while now_height < need_height:
    counter += 1
    now_height += add_height
    
print(counter)
