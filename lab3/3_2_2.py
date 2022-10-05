s = int(input('Enter the square: '))
for a in range(1,21):
    if s % a == 0:
        print(f'rectangle is: {a} x {int(s / a)}')
