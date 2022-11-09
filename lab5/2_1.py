from random import randint
"""
Дана матрица размера M × N и целые числа K1 и K2 (1 ≤ K1 < K2 ≤ N). Поменять местами столбцы матрицы с номерами K1 и K2. 

"""
N = randint(7, 10) # столбцы
M = randint(7, 10) # строки
A = [[0]*M for i in range(N)]
k1 = min(N,M) - randint(1,min(N,M))
k2 = min(N,M) - randint(1,min(N,M))
print(N,M)
print(k1,k2)
for i in range(N):
    for j in range(M):
        A[i][j] = randint(-20, 20)

for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()

for j in range(N):
    A[j][k1], A[j][k2] = A[j][k2], A[j][k1]

print("-------------------------------------")
for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()

