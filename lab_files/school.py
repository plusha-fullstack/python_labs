"""
Создать текстовый файл с произвольной информацией.
 Организовать просмотр содержимого файла. «Школьник»:
 фамилия; имя; отчество; пол; национальность; рост;
 вес; дата рождения (год, месяц число); номер телефона;
 класс. Вывести сведения про всех учеников пятых классов.
  Организовать чтение и обработку
данных из файла в соответствии с индивидуальным заданием.
Сохранить полученные результаты в новый текстовый файл
"""
fin = open("in.txt", "r", encoding="utf8")
fout = open("out.txt","w")
while True:
    s = fin.readline()
    if not s:
        break
    arr = s.split()
    if arr[-1] == '5':
        fout.write(s)

fin.close()
fout.close()
