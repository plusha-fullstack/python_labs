from random import randint
"""
Дана матрица размера M × N. Вставить в нее строку из некоторого числа K1  перед строкой,
среднеарифметическое значение элементов которой минимально.
"""
N = randint(7, 10) # столбцы
M = randint(7, 10) # строки
k1 = [-1] * N
A = [[0]*M for i in range(N)]
print(N,M)
for i in range(N):
    for j in range(M):
        A[i][j] = randint(-20, 20)

sr = 100000
index = 0
for i in range(N):
    middle = 0
    for j in range(M):
        middle += A[i][j]
    middle = middle / M
    if middle < sr:
        sr = middle
        index = i

for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()


A.insert(index,k1)


print("-------------------------------------")
for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()
