n = int(input('Enter the number: '))
s = 0
for i in range(1,n // 2):
    if i % 2 == 1 and n % i == 0:
# является ли 1 делителем ?
        s += i
print(s)
