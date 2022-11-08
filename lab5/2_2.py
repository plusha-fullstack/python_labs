from random import randint

N = randint(7, 10) # столбцы
M = randint(7, 10) # строки
A = [[0]*M for i in range(N)]
print(N,M)
for i in range(N):
    for j in range(M):
        A[i][j] = randint(-20, 20)

maxx = A[0][0]
index = 0
for i in range(N):
    for j in range(M):
        if A[i][j] > maxx:
            maxx = A[i][j]
            index = j


for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()
for i in range(len(A)):
    A[i].pop(index)

print("-------------------------------------")
for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()
