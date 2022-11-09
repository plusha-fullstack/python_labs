from random import randint
"""
  Дана квадратная матрица A(N, N) целых чисел. Найти сумму S1 элементов в последней строке матрицы. 
  Определить количество элементов под главной диагональю матрицы, значения которых меньше S1.
"""
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
        print("\t%4d" % (A[i][j]), end=' ')
    print()

