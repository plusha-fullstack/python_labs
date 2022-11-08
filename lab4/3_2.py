arr1 = [11, 0, 5, -12, 66, 71, 57, 90, -98, 44, 12, 13, 4]
arr2 = [-7, 3, 14, 15, 90, 111, -67, -23, 11, 12, 44, 88, 55]
itog = []
for i in range(len(arr1)):
    itog.append(max(arr1[i], arr2[i]))

print(itog)
