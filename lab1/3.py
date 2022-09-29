x1,y1,x2,y2,x3,y3 = map(int,input().split())
r1 = ((x2 - x1)**2 +(y2 - y1)**2)**0.5
r2 = ((x3 - x2)**2 +(y3 - y2)**2)**0.5
r3 = ((x3 - x1)**2 +(y3 - y1)**2)**0.5
perimetr = r1 + r2 + r3
half_perimetr = perimetr / 2
square = round((half_perimetr*(half_perimetr - r1) * (half_perimetr - r2) * (half_perimetr - r3))**0.5)
print(perimetr)
print(square)
