s = set('abcdefghijklmnopqrstuvwxyz')
str = 'abcd abc ./-abc 55'
for elem in s:
    if elem in str:
        print(elem,end=' ')
