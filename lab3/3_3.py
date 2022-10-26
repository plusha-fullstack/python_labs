import math
x1,x2 = map(int,input("введите x1 и x2: ").split())
N,m = map(int,input("введите N и m: ").split())
h = (x2-x1)/m
while x2 >= x1:
    s_x = 0
    for i in range(N):
        s_x += ((-1) ** i) * ((x1 ** (2 * i)) / math.factorial(2 * i))
    print(format(x1,'.3f'),' - ',format(s_x,'.3f'))
    x1+=h
        
