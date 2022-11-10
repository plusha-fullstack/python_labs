a = {1,2,3,4}
b = {2,4,6,7}
c = {9,1,3,5}
d = {5,7,2,8}
print(c|d)
print(a&d)
print(d-b)
print(c^a)

print("____________________________")
print(c)
c.add(0)
print(c)
print("____________________________")
print(a)
a.discard(3)
print(a)
