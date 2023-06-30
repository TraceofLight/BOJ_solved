# Judging Moose

left_tines, right_tines = map(int, input().split())

if not left_tines and not right_tines:
    print('Not a moose')

elif left_tines == right_tines:
    print(f'Even {left_tines * 2}')
    
else:
    print(f'Odd {max(left_tines, right_tines) * 2}')
