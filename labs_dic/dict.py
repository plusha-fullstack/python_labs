dictionary = {}
fin = open("dictionary.txt", encoding="utf8")
while True:
    s = fin.readline()
    if not s:
        break
    dictionary[s.split(" - ")[0]] = s.split(" - ")[1].strip()

fin.close()
f_translate = open("text.txt", encoding="utf8")
f_out = open("out.txt", "w", encoding="utf8")
while True:
    string = ""
    s = f_translate.readline()
    if not s:
        break
    tmp = ''
    for c in s:
        if c == ' ' or c == '.' or c == ','  or c == '\n':
            if tmp.lower() in dictionary:
                string += dictionary[tmp.lower()]
                string += c
            else:
                string += tmp
                string += c
            tmp = ''
        else:
            tmp += c
    if tmp:
        if tmp.lower() in dictionary:
            string += dictionary[tmp]
        else:
            string += tmp
        tmp = ''
    f_out.write(string)
