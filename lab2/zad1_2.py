n = int(input())
flag = True
while n > 0:
    digit_right = n % 10
    digit_left = (n // 10) % 10
    if digit_left > digit_right:
        flag = False
    n = n // 10
print(flag)
