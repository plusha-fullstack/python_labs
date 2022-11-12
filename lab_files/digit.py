"""
Дан файл, в каждой строке которого
записаны числа. Найти сумму четных чисел
строки и результат в восьмеричной системе
записать в другой файл
"""

sum = 0
fin = open("in.txt", "r")
while True:
    s = fin.readline().split()
    for ele in s:
        if int(ele) % 2 == 0:
            sum += int(ele)
    if not s:
        break

fin.close()
sum = oct(sum)
fout = open("out.txt","w")
fout.write(str(sum))
