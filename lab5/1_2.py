from random import randint

N = randint(3, 10) # столбцы
M = randint(3, 10) # строки
A = [[0]*M for i in range(N)]

print(N, M)
for i in range(N):
    for j in range(M):
        A[i][j] = randint(-20, 20)

for i in range(N):
    summ = 0
    count = 0
    for j in range(M):
        if A[i][j] < 0:
            summ += A[i][j]
            count += 1
    print(f"Для строки {i} среднее арифметическое отрицательных  = {summ/count}")


for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

