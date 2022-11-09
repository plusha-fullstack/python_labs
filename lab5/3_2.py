from random import randint

"""
Дана целочисленная матрица A(N, N), заполненная целыми числами.
Отсортировать по возрастанию элементы матрицы,
от первого элемента до первого минимального элемента матрицы.
"""
N = randint(7, 10) # столбцы
A = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = randint(-20, 20)

tmp = []

for i in range(N):
    for j in range(N):
        if j < i:
            tmp.append(A[i][j])

index = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()
print("-------------------------------------")
tmp.sort(reverse=True)
for i in range(N):
    for j in range(N):
        if j < i:
            A[i][j] = tmp[index]
            index += 1

for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()

