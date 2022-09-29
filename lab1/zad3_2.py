from math import sin
x,y = map(float,input().split())
print(x >= 0 and y < 0.5 and y < sin(x) and y >= 0 )
