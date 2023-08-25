# Rulltrappa

total_stair, movement, go_up = map(int, input().split())
left_get_on_time, right_get_on_time = map(float, input().split())
left_people, right_people = map(int, input().split())

left_time = left_people / left_get_on_time + total_stair / go_up
right_time = right_people / right_get_on_time + total_stair / movement

if left_time > right_time:
    print("latmask")
else:
    print("friskus")
