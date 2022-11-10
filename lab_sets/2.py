def card(s):
    M = set(range(0, 99))
    counter = 0
    for element in s:
        if element in M:
            counter += 1
    return counter
"""
Задача 2 type M = set of 0..99;Описать функцию card (А) ,
подсчитывающую количество элементов, в множестве А типа  М. 
Составить программу, использующую эту функцию.
"""

a = {1,2,3,4,"a",5,"d"}
print(card(a))
