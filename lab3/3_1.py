n = int(input('Enter the number: '))
digit = int(input('Recognzing digit: '))
flag = False
multy = 1
while n > 0:
    curr = n % 10
    if digit == curr:
        flag = True
    multy *= curr
    n = n // 10
    
print('Is Recognzing digit in number:',flag)
print('Multyplication =',multy)
