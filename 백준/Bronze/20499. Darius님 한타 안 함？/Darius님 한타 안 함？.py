# Darius님 한타 안 함?

kill, death, assist = map(int, input().split('/'))

if kill + assist < death or not death:
    print('hasu')
else:
    print('gosu')
