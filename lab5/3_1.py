from random import randint

N = randint(7, 10) # столбцы
posivitive = []
others = []
A = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = randint(-20, 20)


for i in range(N):
    for j in range(N):
        if A[i][j] > 0:
            posivitive.append(A[i][j])
        else:
            others.append(A[i][j])


for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%4d" % (A[i][j]), end=' ')
    print()
print("-------------------------------------")
print(posivitive)
print("-------------------------------------")
print(others)
