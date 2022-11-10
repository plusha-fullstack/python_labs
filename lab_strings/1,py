word = "АБВГДЕЖ А В"
word = list(word)
for i in range(len(word)):
    if word[i] == 'А': # здесь кириллица
        word[i] = 'В'
    elif word[i] == 'В':
        word[i] = 'А'

word = ''.join(word)
print(word)


def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


word = "АБВГДЕЖ А В"
for i in range(len(word)):
    if word[i] == 'А':
        word = replace_str_index(word,i,'В')
    elif word[i] == 'В':
        word = replace_str_index(word,i,'А')

print(word)
