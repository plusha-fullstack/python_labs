def first_positive(array: list, delim: int):
    for i in array:
        if i % delim == 0 and i > 0:
            return i


def delete_min_max(array: list):
    array.pop(array.index(max(array)))
    array.pop(array.index(min(array)))


def inserting_zeros(array: list):
    i = 0
    while i < len(array):
        if arr[i] == 0:
            array.insert(i, "x")
            i += 2
        else:
            i += 1


arr = [0,-4, 2, 1, 8, 0, 9, 51, 90, 0, 11, 44, -6, 17, 0]
"""
В одномерном массиве, состоящем из п целых элементов, найти первый положительный элемент кратный целому числу d.
В одномерном массиве, состоящем из п целых элементов удалить минимальный и максимальный элементы.
В одномерный массив, состоящий из п целых чисел вставить новый элемент перед всеми нулевыми элементами.
"""
d = int(input())
if first_positive(arr, d) is None:
    print("Не удалось найти подобное число")
else:
    print("Первый положительный кратный ", d, " это ", first_positive(arr, d))
delete_min_max(arr)
print("Без min max : ", arr)
inserting_zeros(arr)
print("Вставили кресты перед нулями: ", arr)
