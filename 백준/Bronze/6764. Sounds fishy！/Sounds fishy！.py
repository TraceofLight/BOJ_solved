# Sounds fishy!

fish_log = []

for _ in range(4):
    fish_log.append(int(input()))
    
if fish_log[0] < fish_log[1] < fish_log[2] < fish_log[3]:
    print('Fish Rising')
elif fish_log[0] > fish_log[1] > fish_log[2] > fish_log[3]:
    print('Fish Diving')
elif fish_log[0] == fish_log[1] == fish_log[2] == fish_log[3]:
    print('Fish At Constant Depth')
else:
    print('No Fish')
