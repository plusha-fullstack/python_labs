from random import randint

N = randint(3, 10)
A = [[0]*N for i in range(N)]
sum1 = 0
for i in range(N):
    for j in range(N):
        A[i][j] = randint(-20, 20)

for i in range(N):
    sum1 += A[N - 1][i]

print(sum1)


count = 0
for i in range(N):
    for j in range(N):
        if j < i and A[i][j] < sum1:
            count += 1


print(count)
for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%2d" % (A[i][j]), end=' ')
    print()
