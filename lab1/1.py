x1,y1,x2,y2 = map(int,input().split())
print('Площадь = ',abs(x2 - x1) * abs(y2 - y1))
print('Периметр', 2 * (abs(x2 - x1) + abs(y2 - y1)))
