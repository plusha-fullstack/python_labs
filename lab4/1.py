arr = [-4, 2, 1, 8, 9, 51, 90, 11, 44, -6, 17]
"""
В одномерном массиве, состоящем из п целых элементов, вычислить:
1)количество и сумму  положительных элементов массива;
2)наибольший элемент из отрицательных и его номер и  наименьший элемент из положительных и его номер;
3)среднее арифметическое всех элементов массива, имеющих нечетное значение.

"""
count_of_positives = 0
sum_of_positives = 0
negative_max = -100000
negative_max_id = 0
flag_negative = False
positive_min = 1000000
positive_min_id = 0
flag_positive = False
middle_odd = 0
odd_count = 0
for i in range(len(arr)):
    if arr[i] > 0:
        count_of_positives += 1
        sum_of_positives += arr[i]
        if arr[i] < positive_min:
            flag_positive = True
            positive_min = arr[i]
            positive_min_id = i
    if arr[i] < 0:
        if arr[i] > negative_max:
            flag_negative = True
            negative_max = arr[i]
            negative_max_id = i
    if arr[i] % 2 == 1:
        middle_odd += arr[i]
        odd_count += 1

middle_odd = middle_odd / odd_count

print("Количество положительных: ", count_of_positives, "Их сумма: ",sum_of_positives)
if flag_negative:
    print("номер элема: ",negative_max_id , "наибольший из отрицательных: ", negative_max)
else:
    print("нет отрицательных")

if flag_positive:
    print("номер элема: ", positive_min_id, "наименьший из положительных: ", positive_min)
else:
    print("нет положительных")

print("Среднее арифметическое: ",middle_odd)
