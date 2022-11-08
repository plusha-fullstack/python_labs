arr = [11, 0, 5, -12, 66, 71, 57, 90, -98, 44, 12, 13, 4]
tmp = sorted([x for x in arr if x > 0])
print(tmp)
print(arr)
index = 0
for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] = tmp[index]
        index += 1

print(arr)
